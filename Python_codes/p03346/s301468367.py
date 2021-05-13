n=int(input())
p=[int(input())-1 for _ in range(n)]
ans=[0]*n
for i in p:
  if i!=0:
    ans[i]=ans[i-1]+1
  ans[i]=max(ans[i],1)
print(n-max(ans))