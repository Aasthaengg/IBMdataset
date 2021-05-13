import heapq
n,k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for left in range(n+1):
    for right in range(left, n+1):
        have = []
        heapq.heapify(have)
        i = 0
        while i < left:
            heapq.heappush(have, v[i])
            i += 1
        cost = left + (n - right)
        if cost > k:
            continue
        i = n-1
        while i >= right:
            heapq.heappush(have, v[i])
            i -= 1
        while k - cost > 0 and len(have) > 0:
            value = heapq.heappop(have)
            if  value >= 0:
                heapq.heappush(have,value)
                break
            cost += 1
        #print("left:{} right:{} ans:{}".format(left, right, sum(have)))
        ans = max(ans, sum(have))
print(ans)


