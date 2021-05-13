import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()
offset = 10**10

def main():
    """
    ナップサックで重さを飛び飛びにしてdpを軽くしなくても、
    そもそも重さが４パターンだから全探索で解けたのか。。。。。。
    """
    N, W = map(int, input().split())
    item = [[] for _ in range(4)]
    length = [1, 0, 0, 0]
    w0, v0 = map(int, input().split())
    item[0].append(v0)
    for _ in range(N - 1):
        w, v = map(int, input().split())
        item[w - w0].append(v)
        length[w - w0] += 1
    for i in range(4): item[i].sort(reverse=True)

    # 重さの累積和
    S = []
    for i in range(4):
        S.append([0] + list(accumulate(item[i])))

    ans = 0
    for a in range(length[0] + 1):
        for b in range(length[1] + 1):
            for c in range(length[2] + 1):
                for d in range(length[3] + 1):
                    weight = a * w0 + b * (w0 + 1) + c * (w0 + 2) + d * (w0 + 3)
                    if weight > W: continue
                    ans = max(ans, S[0][a] + S[1][b] + S[2][c] + S[3][d])
    print(ans)


if __name__ == "__main__":
    main()
