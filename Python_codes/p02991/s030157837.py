import sys
input = sys.stdin.buffer.readline
from collections import deque

def main():
    N,M = map(int,input().split())
    edge =[[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        edge[u-1].append(v-1)

    S,T = map(int,input().split())
    q = deque()
    go = [[False for _ in range(3)] for _ in range(N)]
    q.append((S-1,0,1))
    while q:
        now,step,d = q.popleft()
        if step == 3:
            if now == T-1:
                print(d)
                exit()
            step = 0
            d += 1
        if go[now][step]:
            continue
        go[now][step] = True
        for fol in edge[now]:
            q.append((fol,step+1,d))

    print(-1)

if __name__ == "__main__":
    main()