def fac(n):
    dic = {}
    cur = n
    for i in range(2,(int(n**0.5)+2)):
        if cur % i == 0:
            count = 0
            while cur % i == 0:
                count += 1
                cur //= i
            dic[i] = count
            if cur == 1:
                break
    if cur != 1:
        dic[cur] = 1
    return dic

def cmb(a,b,c):
    b = min(b,a-b)
    num = 1
    for i in range(b):
        num = num*(a-i) % c
    den = 1
    for i in range(b):
        den = den*(i+1) % c
    return num * pow(den,c-2,c) % c

n,m = map(int,input().split())
mod  = 10**9 + 7
dic = fac(m)
ans = 1
for i in dic.keys():
    x = dic[i]
    ans *= cmb(x+n-1,x,mod)
    ans %= mod
print(ans)