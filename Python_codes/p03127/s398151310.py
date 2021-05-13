
import math
N = int(input())
A = [int(x) for x in input().split()]

ans = A[0]
for a in A[1:]:
    ans = math.gcd(a, ans)

print(ans)


