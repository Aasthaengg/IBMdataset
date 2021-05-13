n=int(input())
p=[int(x) for x in input().split()]


cnt=0
for i in range(n-1):
  if i+1 == p[i]:
    cnt+=1
    p[i+1]=p[i]
  else:
    mae=p[i]

if p[n-1]==n:
  print(cnt+1)
else:
  print(cnt)
