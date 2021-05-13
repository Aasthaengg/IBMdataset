import bisect

N = int(input())
L = sorted(map(int, input().split()))
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = bisect.bisect_left(L, L[i] + L[j])
        if k > j:
            ans += k - j - 1
print(ans)
