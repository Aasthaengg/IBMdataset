
def hoge():

    n, p = [int(c) for c in input().split()]
    s = input()    

    if p in (2,5):
        a = tuple(int(c)%p for c in s)
        out = 0
        for i,x in enumerate(a):
            if x==0:
                out += (i + 1)
    else:
        a = [0]*n
        tmp = 0
        for i in reversed(range(n)):
            tmp = (tmp + pow(10, n-i-1, p) * int(s[i])) % p
    #         tmp = (tmp + 10**(n-i-1) * int(s[i])) % p
            a[i] = tmp
        d = {i: 0 for i in range(p)}
        d[0] = 1
        out = 0
        for x in a[::-1]:
            out += d[x]
            d[x] += 1
    print(out)
hoge()