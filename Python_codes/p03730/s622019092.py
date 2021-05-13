a,b,c = map(int, input().split())
import math
abgcd = math.gcd(a,b)
ans = "YES" if c%abgcd == 0 else "NO"
print(ans)