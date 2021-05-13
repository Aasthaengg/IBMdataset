N=int(input())
ans=float("inf")
for i in range(1,N):
   a,b=map(int,list(str(i))),map(int,list(str(N-i)))
   ans=min(ans,sum(a)+sum(b))
print(ans)