A,B=map(int,input().split())
ans=0

for i in range(A,B+1):
  temp=[x for x in str(i)]
  if temp==temp[::-1]:
    ans+=1
print(ans)