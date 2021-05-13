import heapq, copy
n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = -10 ** 10
for a in range(min(n, k) + 1):
    have = []
    for i in range(a):
        have.append(v[i])

    o_have = copy.deepcopy(have)

    for b in range(min(n, k) - a + 1):
        for i in range(b):
            have.append(v[n-i-1])

        heapq.heapify(have)
        # print(1, have)
        for c in range(k - a - b):
            if len(have) <= 0:
                break
            item = heapq.heappop(have)
            # print(c, item, have)
            if item >= 0:
                have.append(item)
                break
        ans = max(ans, sum(have))
        # print(2, have, ans, a, b)
        have = copy.deepcopy(o_have)

print(ans)
