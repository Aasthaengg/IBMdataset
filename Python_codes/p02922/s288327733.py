A,B=map(int,input().split())
for i in range(B):
  if(i*A-i+1>=B):
    ans=i
    break
print(ans)