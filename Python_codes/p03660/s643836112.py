from collections import deque
N = int(input())
G = {}
for i in range(N-1):
    a,b = map(int,input().split())
    if a not in G:
        G[a] = []
    G[a].append(b)
    if b not in G:
        G[b] = []
    G[b].append(a)
hist = [-1 for _ in range(N+1)]
heapF = deque([(1,0)])
hist[1] = 0
heapS = deque([(N,0)])
hist[N] = 1
turn = 0
while heapF or heapS:
    if turn%2==0:
        while heapF:
            cur = heapF.popleft()
            if cur[1]==turn//2:
                for x in G[cur[0]]:
                    if hist[x]<0:
                        heapF.append((x,cur[1]+1))
                        hist[x] = 0
            else:
                heapF.append(cur)
                break
    else:
        while heapS:
            cur = heapS.popleft()
            if cur[1]==turn//2:
                for x in G[cur[0]]:
                    if hist[x]<0:
                        heapS.append((x,cur[1]+1))
                        hist[x] = 1
            else:
                heapS.append(cur)
                break
    turn += 1
n = hist.count(0)
m = hist.count(1)
if m>=n:
    print("Snuke")
else:
    print("Fennec")