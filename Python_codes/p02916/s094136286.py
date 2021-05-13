n=int(input())
aa=list(map(int,input().split()))
bb=list(map(int,input().split()))
cc=list(map(int,input().split()))

ans=0
for i in range(n):
  ans+=bb[aa[i]-1]
  if i>0 and (aa[i]-1)==aa[i-1]:
    ans+=cc[aa[i-1]-1]
    
print(ans)