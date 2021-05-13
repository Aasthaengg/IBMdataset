import heapq,copy

N,K = (int(x) for x in input().split())
V = list(map(int, input().split()))
v = copy.copy(V)
ans = 0
if N <= K:
    heapq.heapify(v)
    for i in range(min(K-N,len(v))):
        temp = heapq.heappop(v)
        if temp >= 0:
            ans = max(ans,sum(v)+temp)
            break
    else:
        ans = max(ans,sum(v))
for i in range(min(N,K+1)):
    for j in range(min(N,K+1)-i):
        if (i == 0 and j == 0) or i + j == N:
            continue
        else:
            l = V[:j] + V[N-1:N-1-i:-1]
            heapq.heapify(l)
            for k in range(min(K-i-j,len(l))):
                temp = heapq.heappop(l)
                if temp >= 0:
                    ans = max(ans,sum(l)+temp)
                    break
            else:
                ans = max(ans,sum(l))
print(ans)