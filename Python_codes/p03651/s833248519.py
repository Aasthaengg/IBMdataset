from fractions import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))
n = a[0]
max_num = max(a)
for num in a[1:]:
    n = gcd(n, num)
if k % n == 0 and k <= max_num:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")