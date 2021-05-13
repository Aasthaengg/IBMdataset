N,K=map(int,input().split())

a=N//K

ans=min(abs(N-a*K), abs(N-(a+1)*K))
print(ans)