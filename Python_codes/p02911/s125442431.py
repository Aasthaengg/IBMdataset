n,k,q=[int(x) for x in input().split()]
l=[k-q]*n
for i in range(q):
  p=int(input())
  l[p-1]+=1
for i in range(n):
  if l[i]>0:
    print("Yes")
  else:
    print("No")