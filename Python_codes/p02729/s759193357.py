import sys
import math
N,M = map(int,input().split())

if not ( 0 <= N <= 100 and 0 <= M <= 100 ): sys.exit()
if not ( 2 <= N+M ): sys.exit()
if not ( isinstance(N,int) and isinstance(M,int) ): sys.exit()

ans = 0
if N >= 2:
    ans += math.factorial(N) // (math.factorial(N - 2) * math.factorial(2))
if M >= 2:
    ans += math.factorial(M) // (math.factorial(M - 2) * math.factorial(2))
print(ans)