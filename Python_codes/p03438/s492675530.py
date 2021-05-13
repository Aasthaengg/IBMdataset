n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = sum(b)-sum(a)
res=0
for i in range(n):
  if b[i]>a[i]:
    res += (b[i]-a[i]+1)//2
if res > t:
  print('No')
else:
  print('Yes')