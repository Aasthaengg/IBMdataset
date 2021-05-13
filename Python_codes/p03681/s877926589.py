import math
n, m = map(int, input().split())
div = 10**9 + 7

if abs(n-m)>1:
    print(0)
    exit()
elif n == m:
    ans1 = math.factorial(n)
    ans2 = math.factorial(m)
    ans = 2 * ans1 * ans2 
else:
    ans1 = math.factorial(n)
    ans2 = math.factorial(m)
    ans = ans2*ans1

print(ans % div)