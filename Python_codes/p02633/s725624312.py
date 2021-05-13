X = int(input())
import math
A = X // math.gcd(360, X)
ans = 360 * A // X
print(ans)