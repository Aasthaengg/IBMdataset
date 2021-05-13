ans=float("Inf")
N=int(input())
l=list(input())
W=0
E=l.count("E")
for i in range(N):
   if l[i]=="W":
      ans=min(ans,W+E)
      W+=1
   else:
      E-=1
      ans=min(ans,W+E)
print(ans)