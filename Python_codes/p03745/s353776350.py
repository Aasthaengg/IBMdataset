N= int(input())
now=0
ans=1
S=0
l=list(map(int,input().split()))
for i in range(1,N):
   X=l[i]-l[i-1]
   X=0 if X==0 else 1 if X>0 else -1
   if X==0:
      continue
   elif S ==0:
      S=X
   elif S != X:
      ans+=1
      S=0
print(ans)