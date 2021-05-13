from math import gcd
n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, n):
    ans = gcd(ans, a[i])
cnt = 0
while ans % 2 == 0:
    ans //= 2
    cnt += 1
print(cnt)