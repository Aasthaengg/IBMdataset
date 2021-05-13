H,N=map(int,input().split())
l=list(map(int,input().split()))
total=0
for k in range(N):
  total+=l[k]
if total>=H:
  print("Yes")
else:
  print("No")