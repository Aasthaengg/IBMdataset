def cmb(n, r):
    if n - r < r: r = n - r
    if r < 0 : return 0
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


n,a,b=map(int,input().split())
v=list(map(float,input().split()))
v=sorted(v,reverse=True)
V=0
for i in range(a):
  V=V+v[i]
ans1=V/a
print(ans1)
ans2=0
if v[0]==ans1:
  c=v.count(ans1)
  for i in range(a,b+1):
    ans2=ans2+cmb(c,i)
  print(ans2)
else:
  d=0
  e=0
  for i in range(a):
    if v[i]==v[a]:
      d=d+1
  for i in range(n):
    if v[i]==v[a]:
      e=e+1
  ans2=cmb(e,d)
  print(ans2)