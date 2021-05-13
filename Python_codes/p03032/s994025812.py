import heapq, copy
n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = -10 ** 10
for a in range(k + 1):
    for b in range(k - a + 1):
        if a + b > min(k, n):
            break
        # print(a, b)
        have = v[:a] + v[n-b:]
        # print(have)

        tmp = sum(have)
        ans = max(ans, tmp)

        have.sort()

        c = k - a - b

        for item in have:
            if c <= 0:
                break
            c -= 1
            if item >= 0:
                break

            tmp -= item
            ans = max(ans, tmp)

print(ans)