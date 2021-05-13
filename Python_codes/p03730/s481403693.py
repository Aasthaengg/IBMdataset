import math
a,b,c = map(int,input().split())
print("YES" if 0 == c%math.gcd(a,b) else "NO")