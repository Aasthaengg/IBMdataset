N = int(input())
import math
ans = int(input())
for i in range(N - 1):
    a = int(input())
    ans = a * ans // math.gcd(a, ans)
print(ans)