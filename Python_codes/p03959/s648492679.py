n = int(input())
a = list(map(int,input().split()))
t = list(map(int,input().split()))
if n == 1:
  if a[0] == t[0]:
    print(1)
  else:
    print(0)
  quit()
mod = 10**9+7
h = [[1,10**12] for i in range(n)]
h[0] = [a[0],a[0]]
h[-1] = [t[-1],t[-1]]
for i in range(1,n-1):
  h[i][1] = min(h[i][1],a[i])
  if a[i-1] < a[i]:
    h[i][0] = a[i]
for i in range(n-2,0,-1):
  h[i][1] = min(h[i][1],t[i])
  if t[i+1] < t[i]:
    h[i][0] = t[i]
ans = 1
for i in range(n):
  if h[i][0] > h[i][1]:
    print(0)
    quit()
  ans = (ans*(h[i][1]-h[i][0]+1))%mod
print(ans)