import sys
input = sys.stdin.buffer.readline
from collections import deque

def main():
    N,M = map(int,input().split())
    edge =[[[] for _ in range(3)] for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        for i in range(3):
            edge[u-1][i].append((v-1,(i+1)%3))

    S,T = map(int,input().split())
    go =[[0 for _ in range(3)] for _ in range(N)]
    q = deque([(S-1,0)])
    while q:
        now,rest = q.popleft()
        for fol,fr in edge[now][rest]:
            if go[fol][fr] == 0:
                go[fol][fr] = go[now][rest]+1
                q.append((fol,fr))
                
    if go[T-1][0] != 0 and go[T-1][0]%3 == 0:
        print(go[T-1][0]//3)
        exit()
    
    print(-1)

if __name__ == "__main__":
    main()
