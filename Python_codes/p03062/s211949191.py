n = int(input())
a = list(map(int, input().split()))

ans = 0
min_a = 10**9+1
flg = False
for i in range(n):
    ans += abs(a[i])
    if a[i] <= 0:
        flg = not flg
    min_a = min(min_a, abs(a[i]))

if flg:
    ans -= 2*min_a

print(ans)
