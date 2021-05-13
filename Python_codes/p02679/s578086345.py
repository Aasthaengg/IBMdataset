## coding: UTF-8
import math
MOD = 10**9+7
N = int(input())
#A = []
#for i in range(N):
    #A.append(list(map(int,input().split()))) 
d = dict()
'''
def bisection(a, n, p):
    #二分累乗法によるO(log p)計算
    bin_str = format(n, 'b')
    res = 1
    tmp = a
    for i in range(1, len(bin_str)+1):
        if(bin_str[(-1)*i] == '1'):
            res = res * tmp % p
        tmp = tmp * tmp % p
    return res
'''
d['a'] = 0
d['b'] = 0
d['c'] = 0

for i in range(N):
    #l = list(map(int,input().split()))
    #l = A[i]
    a,b=map(int,input().split())
    #if(l[0] == 0):
    if(a == 0):
        #if(l[1] == 0):
        if(b == 0):
            d['c'] += 1
        else:
            d['b'] += 1
    #elif(l[1] == 0):
    elif(b == 0):
        d['a'] += 1
    else:
        #g = math.gcd(l[0], l[1])
        g = math.gcd(a, b)
        #a = int(l[0]/g)
        #b = int(l[1]/g)
        a = a//g
        b = b//g
        if(a<0):
            p = (-1*a, -1*b)
        else:
            p = (a, b)
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    #print('i:{}, l[0]:{}, l[1]:{}, d:{}'.format(i, l[0], l[1], d))

#res = 1
a = d.pop('a')
b = d.pop('b')
#あとで二分累乗法に変換する4 
#if(a > 0 and b > 0):
    #a, b>=0 より、a+b>=0, よってa==0 and b == 0でなければ、a >0 or b> 0
    #ma = bisection(2, a, MOD)
    #mb = bisection(2, b, MOD)
    #res *= ma + mb -1
res = pow(2, a, MOD) + pow(2, b, MOD) - 1
res %= MOD

#elif(a == 0 and b > 0):
    #mb = bisection(2, b, MOD)
    #res *= mb
    #res %= MOD
#elif(a > 0 and b == 0):
    #ma = bisection(2, a, MOD)
    #res *= ma
    #res %= MOD
c = d.pop('c')

#print('a:{}, b:{}, c:{}'.format(a,b,c))
#print('d:{}, len(d):{}'.format(d, len(d)))
#print('res', res)

while len(d) > 0:
    s, v = d.popitem()
    if(s[1] < 0):
        opposite = (-1*s[1], s[0])
    else:
        opposite = (s[1], -1*s[0])
    if opposite in d:
        t = d.pop(opposite)
        #print('s:{}, v:{}, opposite:{}, t:{}, d:{}, len(d):{}'.format(s, v, opposite, t, d, len(d)))
        #mv = bisection(2, v, MOD)
        #mt = bisection(2, t, MOD)        
        #res *= mv + mt - 1
        res *= pow(2, v, MOD) + pow(2, t, MOD) - 1
        res %= MOD
    else:
        #print('s:{}, v:{}, opposite:{},       d:{}, len(d):{}'.format(s, v, opposite, d, len(d)))
        #mv = bisection(2, v, MOD)        
        #res *= mv
        res *= pow(2, v, MOD)
        res %= MOD
    #print('res', res)


res += c
res = (res + MOD - 1) % MOD

print(res)