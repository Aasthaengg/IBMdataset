n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(n):
  if a[i]%2!=0:
    cnt=cnt+1
if cnt%2!=0:
  print("NO")
else:
  print("YES")