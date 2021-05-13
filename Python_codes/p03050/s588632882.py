def divisor(n):
    fac = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0: 
            fac.append(i)
            if i*i != n: fac.append(n//i)
    return sorted(fac)

n = int(input())
ans = 0
for i in divisor(n):
    if i == 1: continue
    m = i-1
    p,r = divmod(n,m)
    if p == r: ans += m
print(ans)