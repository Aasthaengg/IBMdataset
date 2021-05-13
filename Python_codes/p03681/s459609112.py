import math

N, M = map(int,input().split())
a = 10**9 + 7


if abs(N - M) >= 2:
    print(0)
    exit()
elif abs(N-M) == 1:
    ans = math.factorial(N)*math.factorial(M) % a
else:
    ans = 2*math.factorial(N)*math.factorial(M) % a

print(ans)
