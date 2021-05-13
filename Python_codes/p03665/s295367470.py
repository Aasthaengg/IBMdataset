n,p = map(int,input().split())
a = [int(i) for i in input().split()]

fac = [1]*(n+1)
for i in range(2,n+1): fac[i] = fac[i-1]*i
def comb(n,k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n]//(fac[k]*fac[n-k])

even = odd = 0
for i in range(n):
    if a[i]%2 == 0: even += 1
    else: odd += 1

cnte = cnto = 0
for i in range(even+1): cnte += comb(even,i)
for i in range(odd+1)[p::2]: cnto += comb(odd,i)
print(cnte*cnto)