k,x=map(int,input().split())

ans=''
for i in range(x-k+1,x+k):
  if abs(i)<=2000000:
    ans+=str(i)+' '
print(ans)