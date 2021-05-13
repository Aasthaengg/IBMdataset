N = int(input())

r = []
l = []
for i in range(N):
  ri, li = input().split()
  r.append(int(ri))
  l.append(int(li))
  
ans=0
for i in range(N):
  #print(r[i],l[i])
  ans=ans-r[i]+l[i]+1
print(ans)
