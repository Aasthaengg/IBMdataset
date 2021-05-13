N = int(input())
L = list(map(int, input().split()))

L.sort()

# print(L)
import bisect
ans = 0
for i in range(N-2):
    l1 = L[i]
    for j in range(i+1, N-1):
        l2 = L[j]
        l3_max = (l1 + l2)

        k = bisect.bisect_left(L, l3_max, lo=j+1)
        ans += max(0, k - j - 1)
print(ans)