n=int(input())
p=list(map(int,input().split()))
ans=0
for i in range(1,n-1):
  temp=list()
  temp.append(p[i-1])
  temp.append(p[i])
  temp.append(p[i+1])
  if p[i]==sorted(temp)[-2]:
    ans+=1
print(ans)