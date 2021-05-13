import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    repn = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        repn[a - 1].append(b - 1)
        repn[b - 1].append(a - 1)

    """
    改良コードも試す。
    どっちが先にマスに色を塗るかは、要は両者のスタート地点からの距離を比べれば良い。
    前にもこの手の議論見た気がする。。。
    """

    # FennecとSnukeからのdepthを求める
    depth_from_Fennec = [-1] * N
    depth_from_Snuke = [-1] * N
    depth_from_Fennec[0] = 0
    depth_from_Snuke[N - 1] = 0

    q = deque([0])
    while q:
        u = q.popleft()
        for v in repn[u]:
            if depth_from_Fennec[v] != -1: continue
            depth_from_Fennec[v] = depth_from_Fennec[u] + 1
            q.append(v)
    q.append(N - 1)
    while q:
        u = q.popleft()
        for v in repn[u]:
            if depth_from_Snuke[v] != -1: continue
            depth_from_Snuke[v] = depth_from_Snuke[u] + 1
            q.append(v)

    Fennec = Snuke = 0
    for f, s in zip(depth_from_Fennec, depth_from_Snuke):
        if f <= s:
            Fennec += 1
        else:
            Snuke += 1
    if Fennec > Snuke:
        print("Fennec")
    else:
        print("Snuke")


if __name__ == "__main__":
    main()
