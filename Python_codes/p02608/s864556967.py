n = int(input())
sqn = int(n**0.5)+1
f = [0] * (n+1)
for x in range(1,sqn):
    for y in range(1, sqn):
        for z in range(1, sqn):
            nn = x*x + y*y + z*z + x*y + y*z + z*x
            if nn <= n : f[nn]+=1
for i in range(1,n+1):
    print(f[i])