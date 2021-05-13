N=int(input())
A=[int(x) for x in input().split()]
ans=[0]*N
for a in A:
  ans[a-1]+=1
for a in ans:
  print(a)