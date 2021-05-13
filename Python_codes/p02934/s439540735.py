n = int(input())
a = list(map(int,input().split()))
deno = 1
nume = 0.0
         
for i in range(n):
         deno *= a[i]
for j in range(n):
         nume_frac = deno / a[j]
         nume = nume + nume_frac
         
print((deno / nume))