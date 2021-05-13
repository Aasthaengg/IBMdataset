N = int(input())
import math
ans = math.factorial(N)
ans %= 1000000007
print(ans)