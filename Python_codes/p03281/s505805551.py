n = int(input())
              
def primes(n):
    p = []    
    i = 1     
    while True:
        i += 1
        if i * i > n:
            break
        ok = True
        for j in p:
            if i % j == 0:
                ok = False
                break
        if ok:
            p.append(i)
    return p  
p = primes(n) 
              
ans = 0       
for i in range(1, len(p)):
    for j in range(i+1, len(p)):
        for k in range(j+1, len(p)):
            if p[i] * p[j] * p[k] <= n:
                ans += 1
              
for i in range(1, len(p)):
    for j in range(i+1, len(p)):
        if p[i] * p[i] * p[i] * p[j] <= n:
            ans += 1
print(ans)

