n = int(input())
a = list(map(int, input().split()))
m = 0
for i,j in enumerate(a):
  if i%2==1:
    m+=-1*j
  else:
    m+=j
ans = [m]
for i in a[:-1]:
  b = -1*m+2*i
  ans.append(b)
  m = b
print(' '.join(map(str,ans)))