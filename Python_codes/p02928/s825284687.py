n,k = map(int,input().split())
a = list(map(int,input().split()))
l = [0]*n
r = [0]*n
for i in range(n):
  for j in range(n):
    if a[i] > a[j]:
      if j < i:
        l[i] += 1
      if j > i:
        r[i] += 1
#print(l)
#print(r)
ans = 0
MOD = 1000000007
x = (k*(k-1)//2)%MOD
y = (k*(k+1)//2)%MOD
for i in range(n):
  ans = (ans + x*l[i] + y*r[i])%MOD
print(ans)