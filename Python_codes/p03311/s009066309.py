n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= i + 1
a.sort()
if n % 2:
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b)
    print(ans)
else:
    b1 = (a[n//2-1] + a[n//2] + 1) // 2
    b2 = (a[n//2-1] + a[n//2]) // 2
    ans1, ans2 = 0, 0
    for i in range(n):
        ans1 += abs(a[i] - b1)
        ans2 += abs(a[i] - b2)
    print(min(ans1, ans2))
