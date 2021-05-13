n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
i = 0
ans = 0
j = 3 * n - 2
while i < n:
    ans += a[j]
    i += 1
    j -= 2

print(ans)