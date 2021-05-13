n,k=[int(i) for i in input().split()]

p=[int(i) for i in input().split()]

p.sort()
ans=0
for i in range(k):
  ans+=p[i]
  
print(ans)