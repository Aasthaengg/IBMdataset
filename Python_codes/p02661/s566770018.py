n=int(input())
a,b=[],[]
for i in range(n):
  aa,bb=map(int,input().split())
  a.append(aa)
  b.append(bb)

a.sort()
b.sort()
if n%2==1:
  print(b[n//2]-a[n//2]+1)
else:
  a_cnt=a[n//2]+a[n//2-1]
  b_cnt=b[n//2]+b[n//2-1]
  print(b_cnt-a_cnt+1)