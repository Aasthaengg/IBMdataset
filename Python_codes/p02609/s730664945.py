from logging import *
basicConfig(level=DEBUG, format='%(levelname)s: %(message)s')
disable(CRITICAL)

n = int(input())
X = input()
debug('n {}'.format(n))
debug('X {}'.format(X))
po = X.count('1')

# if po == 0:
#     print(0)
#     exit()

pp = po + 1
pm = max(1, po - 1)

rp = 0
rm = 0
for x in X:
    rp = (rp*2 + int(x)) % pp
    rm = (rm*2 + int(x)) % pm

bp = [0]*(n) # 2^i % (po+1)
bm = [0]*(n) # 2^i % (po-1)
bp[n-1] = 1 % pp
bm[n-1] = 1 % pm
for i in range(n-1,0,-1):
    bp[i-1] = bp[i]*2 % pp
    bm[i-1] = bm[i]*2 % pm

debug('po {}'.format(po))
debug('pp {}'.format(pp))
debug('pm {}'.format(pm))
debug('rp {}'.format(rp))
debug('rm {}'.format(rm))
debug('bp {}'.format(bp))
debug('bm {}'.format(bm))
debug('===')

def popcount(x):
    c = 0
    while x > 0:
        if x & 1: c += 1
        x //= 2
    return c

def f(x):
    if x==0: return 0
    return f(x % popcount(x)) + 1

for i in range(n):
    if X[i] == '0':
        ri = (rp + bp[i]) % pp
    else: # '1'
        if po-1 != 0: ri = (rm - bm[i]) % pm
        else:
            print(0)
            continue
    debug('i {} ri {}'.format(i,ri))
    c = f(ri) + 1
    debug('c {}'.format(c))
    print(c)

