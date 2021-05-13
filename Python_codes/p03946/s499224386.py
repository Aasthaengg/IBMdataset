import heapq

N,T = map(int, input().split())
A = [int(a) for a in input().split()]

l = A[0]
l_idx = 0
r = []
for i in range(1, N):
    heapq.heappush(r, (-A[i], i))

b = -r[0][0] - l
h = []
heapq.heappush(h, (-b, l_idx, r[0][1]))
for i in range(1, N-1):
    while r[0][1] <= i:
        heapq.heappop(r)
    if l > A[i]:
        l = A[i]
        l_idx = i
    if b <= -r[0][0]-l:
        b = -r[0][0]-l
        heapq.heappush(h, (-b, l_idx, r[0][1]))
        
used1 = [0]*N
used2 = [0]*N
while h:
    t = heapq.heappop(h)
    if -t[0] < b:
        break
    if used1[t[2]] == 1:
        used1[t[2]] = -1
        used2[t[2]] = -1
    if used2[t[1]] == 1:
        used1[t[1]] = -1
        used2[t[1]] = -1
    if used1[t[1]] == 0:
        used1[t[1]] = 1
    if used2[t[2]] == 0:
        used2[t[2]] = 1
    
cnt1 = 0
cnt2 = 0
for i in range(N):
    cnt1 += max(0, used1[i])
    cnt2 += max(0, used2[i])
    
print(min(cnt1, cnt2))