N=int(input())
a=list(map(int,input().split()))
ans=0
i=0
while i+1<=N-1:
  if a[i]!=a[i+1]:
    i+=1
  else:
    tmp=1
    while i+1<=N-1 and a[i]==a[i+1]:
      tmp+=1
      i+=1
    i+=1
    ans+=(tmp//2)
print(ans)