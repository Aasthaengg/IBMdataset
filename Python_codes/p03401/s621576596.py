n = int(input())
a = list(map(int,input().split()))

sum1 = abs(a[0]) + abs(a[-1])
for i in range(n-1):
    sum1 += abs(a[i] - a[i+1])

for i in range(n):
    ans = sum1
    if i == 0:
        ans -= abs(a[0]) + abs(a[1] - a[0])
        ans += abs(a[1])
        print(ans)
    elif i == n-1:
        ans -= abs(a[-1]) + abs(a[-1] - a[-2])
        ans += abs(a[-2])
        print(ans)
    else:
        ans -= abs(a[i-1] - a[i]) + abs(a[i] - a[i+1])
        ans += abs(a[i-1] - a[i+1])
        print(ans)
