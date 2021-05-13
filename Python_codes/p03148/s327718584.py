N,K = map(int,input().split())
ans = [0 for i in range(N+1)]
food = {}
food1 = []
for i in range(1,N+1):
    food[i] = 0
for i in range(N):
    t,d = map(int,input().split())
    food1.append((d,t))
food1.sort()
syurui = 0
sum = 0
import heapq
x = []
heapq.heapify(x)
for i in range(1,N+1):
    d,t = food1[-i]
    if food[t] == 0:
        if i > K:
            if len(x) == 0:
                break
        sum += d
        food[t] = 1
        syurui += 1
        if i > K:
            y = heapq.heappop(x)
            sum -= y
    else:
        if i <= K:
            sum += d
            heapq.heappush(x,d)
    if syurui == K:
        ans[K] = max(sum + K**2,ans[K])
        break
    else:
        ans[syurui] = max(sum + syurui**2,ans[syurui])
print(max(ans))