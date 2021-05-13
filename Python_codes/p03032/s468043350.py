import heapq, copy
n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = -10 ** 10
for a in range(min(n, k) + 1):
    for b in range(min(n, k) - a + 1):
        have = []
        for i in range(a):
            have.append(v[i])
        for i in range(b):
            have.append(v[-i-1])

        tmp = sum(have)
        # heapq.heapify(have)
        have.sort()
        ans = max(ans, tmp)

        for c in range(k - a - b):
            if c >= len(have):
                break
            item = have[c]
            if item >= 0:
                break

            tmp -= item
            ans = max(ans, tmp)

print(ans)
