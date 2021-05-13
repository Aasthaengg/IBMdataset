n,k = map(int,input().split())
a = sorted(list(map(int,input().split())))
mod = 10**9+7
x = 10**10
count = 0
c=[]
for i in range(n):
    if a[i]!=x:
        if i != 0:
            c.append([x,count])
        x=a[i]
        count = 1
    else:
        count += 1
    
    if i==n-1:
        c.append([x,count])

fact = [1]*(n+1)
inv_fact = [1]*(n+1)
for i in range(n):
    fact[i+1] = fact[i]*(i+1)
    fact[i+1] %= mod
for i in range(n,0,-1):
    if i == n:
        inv_fact[i] = pow(fact[i],mod-2,mod)
    else:
        inv_fact[i] = inv_fact[i+1]*(i+1)
        inv_fact[i] %= mod
        
sum_min = 0
sum_max = 0
b = 0
for i,j in c:
    if n-b < k:
        break
    b += j
    for l in range(max(1,k-n+b),min(k,j)+1):
        sum_min += i*fact[j]*inv_fact[j-l]*inv_fact[l]*fact[n-b]*inv_fact[n-b-k+l]*inv_fact[k-l]
        sum_min %= mod
b = 0
for i,j in c[::-1]:
    if n-b < k:
        break
    b += j
    for l in range(max(1,k-n+b),min(k,j)+1):
        sum_max += i*fact[j]*inv_fact[j-l]*inv_fact[l]*fact[n-b]*inv_fact[n-b-k+l]*inv_fact[k-l]
        sum_max %= mod
        
print((sum_max-sum_min)%mod)