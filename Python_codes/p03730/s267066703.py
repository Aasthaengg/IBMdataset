from fractions import gcd


A, B, C = map(int, input().split())
g = gcd(A, B)
if g == 1 or C % g == 0:
    print("YES")
else:
    print("NO")
