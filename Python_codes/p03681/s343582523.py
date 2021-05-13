import math
N,M = list(map(int,input().split()))

ans_mod=10**9+7
ans=0
if N == M+1 or M == N+1:
    ans=(math.factorial(N)*math.factorial(M))%ans_mod
elif N == M:
    ans=(math.factorial(N)*math.factorial(M)*2)%ans_mod
    
print(ans)