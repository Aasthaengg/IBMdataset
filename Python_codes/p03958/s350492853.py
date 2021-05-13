import heapq

K, T = map(int, input().split())
a = list(map(int, input().split()))
a = [(-a[i], i) for i in range(T)]

heapq.heapify(a)
cake_yesterday = -1
ans = 0

for i in range(K):
    cake1 = heapq.heappop(a)
    if cake1[1] != cake_yesterday:
        cake_yesterday = cake1[1]
        if cake1[0]+1 <= -1:
            heapq.heappush(a, (cake1[0]+1, cake1[1]))
    elif a:
        cake2 = heapq.heappop(a)
        cake_yesterday = cake2[1]
        heapq.heappush(a, (cake1[0], cake1[1]))
        if cake2[0]+1 <= -1:
            heapq.heappush(a, (cake2[0]+1, cake2[1]))
    else:
        if cake_yesterday == cake1[1]:
            ans += 1
        ans += -cake1[0] - 1
        break

print(ans)