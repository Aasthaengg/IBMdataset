import sys


n, k = [int(_) for _ in input().split()]
if k == 0:
    print(n*n)
    sys.exit()
ans = 0
m = n-k
t1 = 0
t2 = 0
t3 = 0
ans += ((m*m - m) // 2) + m
for i in range(k+1, n+1):
    t1 = n-i+1
    t2 = t1 // i
    t3 = t1 % i
    ans += t2 * (i-k)
    if t3 > k:
        ans += t3 - k
print(ans)