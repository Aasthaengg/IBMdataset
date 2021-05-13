import sys
input = sys.stdin.buffer.readline
from collections import deque

def main():
    N,M = map(int,input().split())
    dist = [[] for _ in range(N)]
    
    for i in range(M):
        l,r,d = map(int,input().split())
        dist[l-1].append((r-1,d))
        dist[r-1].append((l-1,-d))
        
    go = [None for _ in range(N)]
    for i in range(N):
        if go[i] is None:
            go[i] = 0
        q = deque([i])
        while q:
            l = q.pop()
            for r,d in dist[l]:
                if go[r] is None:
                    go[r] = go[l] + d
                    q.append(r)
                else:
                    if go[r] - go[l] != d:
                        print("No")
                        exit()
        
    print("Yes")
    
if __name__ == "__main__":
    main()