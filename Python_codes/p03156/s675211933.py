N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
check=[0]*3
for x in P:
  if x<=A:
    check[0]+=1
  elif A<x<=B:
    check[1]+=1
  else:
    check[2]+=1
print(min(check))
