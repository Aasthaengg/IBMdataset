N=int(input())
H=list(map(int,input().split()))
t=0
ans=0
for x in range(N-1):
  if H[x]>=H[x+1]:
    ans+=1
  else:
    if ans>t:
      t=ans
    ans=0
print(max(t,ans))
    
