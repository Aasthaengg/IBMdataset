N=int(input())
A=list(map(int,input().split()))
ans=0
mins=10**10
ct=0
for i in A:
 ans+=abs(i)
 mins=min(mins,abs(i))
 if i<0:
  ct+=1
if ct%2==1:
 ans-=2*mins
print(ans)