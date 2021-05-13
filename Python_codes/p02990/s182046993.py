n,k=map(int,input().split())
mod=10**9+7
def cmb(n, r):#nCr 組合わせ
    if n - r < r: r = n - r
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
  
for i in range(1,k+1):
  if i==1:
    print(n-k+1)
  else:
    if k<i or n-k+1<i:
      print(0)
    else:
      print((cmb(n-k+1,i)*(cmb(k-1,i-1)))%mod)
