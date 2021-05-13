from heapq import heappop, heappush

n,m = map(int, input().split())
s = input()

heap = [(0,n)]
turn = [-1]*(n+1)
turn[-1] = 0
for i in range(n-1, -1, -1):
    if s[i] == "1":
        continue
    while heap and heap[0][1]-i>m:
        heappop(heap)
    if not heap:
        break
    cnt, prev = heap[0]
    turn[i] = cnt+1
    heappush(heap, (turn[i], i))

if turn[0] == -1:
    print(-1)
    exit()
prev_turn=turn[0]
prev_ind = 0
ans = []
for i in range(1, n+1):
    if prev_turn-turn[i] == 1:
        ans.append(i-prev_ind)
        prev_ind = i
        prev_turn = turn[i]
print(*ans)