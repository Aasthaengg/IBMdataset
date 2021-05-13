N=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
total=0
for i in range(1,N):
  total+=l[i]
if l[0]<total:
  print("Yes")
else:
  print("No")