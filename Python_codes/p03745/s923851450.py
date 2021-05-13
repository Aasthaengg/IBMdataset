n = int(input())
a = list(map(int, input().split()))
a.append(a[n - 1])
ans = 1
s = 0
i = 1
while i < n:
    if not(a[s] <= a[i] <= a[i + 1]) and not(a[s] >= a[i] >= a[i + 1]):
        s = i + 1
        ans += 1
    i += 1

print(ans)