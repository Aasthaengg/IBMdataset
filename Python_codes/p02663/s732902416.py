H1,M1,H2,M2,K=map(int,input().split())
time=abs(H2-H1)*60+(M2-M1)
ans=time-K
print(ans)