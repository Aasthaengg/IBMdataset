n=int(input())
li=[int(x) for x in input().split()]
su=[]
for i in range(n-1):
  for j in range(i+1,n):
    su.append(li[i]*li[j])
print(sum(su))