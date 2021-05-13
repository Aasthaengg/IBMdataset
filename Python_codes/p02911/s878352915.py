n,k,q=map(int,input().split())
lst=[0]*n
for i in range(q):
  person=int(input())
  lst[person-1]+=1
for p in range(n):
  temp=k-q+lst[p]
  if temp<=0:
    print("No")
  else:
    print("Yes")