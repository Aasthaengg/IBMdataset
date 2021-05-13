from collections import deque
import sys
input = sys.stdin.readline


def main():
    N, M, P = map(int, input().split())
    edge = [[] for _ in range(N)]
    redge = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        C -= P
        C = -C
        edge[A].append((B,C))
        redge[B].append(A)

    # 0 => N-1の間にある閉路を検出したいので
    # 0とN-1からたどりつけない場所は前処理で取り除く
    
    visited1, visited2 = {0}, {N-1}
    
    stack = [0]
    while stack:
        v = stack.pop()
        for dest, _ in edge[v]:
            if dest in visited1:
                continue
            visited1.add(dest)
            stack.append(dest)
    
    stack = [N-1]
    while stack:
        v = stack.pop()
        for dest in redge[v]:
            if dest in visited2:
                continue
            visited2.add(dest)
            stack.append(dest)
    
    OK = visited1 & visited2
    
    new_edge = [[] for _ in range(N)]
    for s in range(N):
        for t, c in edge[s]:
            if t in OK:
                new_edge[s].append((t,c))

    flag = True
    d = [float('inf')] * N
    d[0] = 0
    #ベルマンフォード法、N回実行してまだ更新されている場合は負の閉路が存在する
    for _ in range(N):
        flag = False
        for v, e in enumerate(new_edge):
            for t, c in e:
                if d[v] != float('inf') and d[v] + c < d[t]:
                    d[t] = d[v] + c
                    flag = True
        if not flag:
            print(max(0,-d[N-1]))
            exit()
    else:
        print(-1)
        exit()


if __name__ == "__main__":
    main()