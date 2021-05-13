N=int(input())
ans=float("Inf")
for i in range(N+1):
   k=N-i
   k2=i
   six=0
   nine=0
   while k2>0:
      six+=k2%6
      k2//=6
   while k>0:
      nine+=k%9
      k//=9
   ans=min(ans,six+nine)
print(ans)