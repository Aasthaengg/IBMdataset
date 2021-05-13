n,x = map(int,input().split())
a = list(map(int,input().split()))
su = 0
for i in range(n-1):
  j,k = a[i],a[i+1]
  if j+k>x:
    t = (j+k)-x
    if k>=t:
      k -= t
      su += t
      a[i+1] = k
    else:
      k = 0
      j -= t-k
      su += t
      a[i+1] = 0
      a[i] = j
print(su)