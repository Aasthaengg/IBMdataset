N = int(input())
T = int(input())
ans = T
import math
for i in range(N - 1):
    T = int(input())
    ans = T * ans // math.gcd(T, ans)
print(ans)