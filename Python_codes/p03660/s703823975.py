import sys
input = sys.stdin.buffer.readline
from collections import deque

def main():
    N = int(input())
    dist = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        dist[a-1].append(b-1)
        dist[b-1].append(a-1)

    def root(x):
        go = [False for _ in range(N)]
        d = [0 for _ in range(N)]
        go[x] = True
        q = deque([x])
        while q:
            now = q.pop()
            for fol in dist[now]:
                if go[fol]:
                    continue
                else:
                    d[fol] = d[now] + 1
                    go[fol] = True
                    q.append(fol)
        return d
    
    fen = root(0)
    snu = root(N-1)
    fg = sg = 0
    for i in range(N):
        if fen[i] <= snu[i]:
            fg += 1
        else:
            sg += 1
            
    print("Fennec" if fg > sg else "Snuke")

if __name__ == "__main__":
    main()
