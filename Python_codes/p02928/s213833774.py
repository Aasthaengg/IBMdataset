n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 +7
inner = 0

for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            inner += 1
            inner %= mod
inner *= k
inner %=mod

outer = 0

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            outer +=1
            outer %= mod
outer *= (k*(k-1)//2)
outer %= mod

print((inner + outer) % mod )

