n=int(input())
s=input()
l=[]
k=len(s.replace(".",""))
ans=n-k
#自分含め左にいくつ黒があるか
cnt=0
#左の黒、右の白
for i in range(n):
  cnt+=int(s[i]=="#")
  ans=min(ans,2*cnt+n-i-1-k)
print(ans)