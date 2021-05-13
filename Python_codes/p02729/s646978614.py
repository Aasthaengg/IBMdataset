import math
n, m = list(map(int, input().split()))
nC2 = math.factorial(n) // (math.factorial(2) * math.factorial(n - 2)) if n >= 2 else 0
mC2 = math.factorial(m) // (math.factorial(2) * math.factorial(m - 2)) if m >= 2 else 0
print(nC2 + mC2)