n = int(input())
mt = 0
ma = 0
for i in range(n):
    t , a = map(int, input().split())
    if t>=mt and a>=ma:
        mt = t
        ma = a
    elif t<mt or a<ma:
        k1 = mt//t
        k2 = ma//a
        k=max(k1,k2)
        while t*k < mt or a*k <ma:
            k+=1
        mt=t*k
        ma=a*k
print(mt+ma)
