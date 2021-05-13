import math
MAX = 10**9 + 7
n,m = map(int,input().split())

ans = 0
if abs(n-m) == 1:
    ans = math.factorial(n)*math.factorial(m) % MAX
elif n == m:
    ans = math.factorial(n)*math.factorial(m)*2 % MAX

print(ans)