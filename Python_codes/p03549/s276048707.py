N,M=map(int,input().split())
p=0.5**M
T=1900*M+100*(N-M)
ans=int(T/p)
print(ans)