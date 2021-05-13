N,M,K = map(int,input().split())
ans = False
for p in range(N+1):
    for q in range(M+1):
        if p*M+q*N - 2*p*q == K:
            ans = True
if ans:print("Yes")
else:print("No")