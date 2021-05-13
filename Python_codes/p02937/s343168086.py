import bisect


def bisect_search(f, val=0, l=0, r=10**6):

    #is_increase=(f(r)-f(l))>=0

    eps = 10**(-5)
    while True:

        c = (l+r)//2
        print(l, c, r)
        input()
        if f(c) == val and f(c-1) != val:
            return c
        #if f(c)-val < eps:
        #    return c

        if f(c) > val:
            r = c

        else:
            l = c

        if l == r:
            return False



def next(ch,k):
    global N,dcs
    k_=k%N
    #print(ch,ch_,k)
    #print(dcs[ch][ch_]+1)
    #print(dcs[ch])
    #print(dcs[ch][ch_]+1)
    #print(N)
    val = dcs[ch][k_-1]+1
    if k_==0:
        val=1

    A=bisect.bisect_left(dcs[ch],val,k_,min(k_+N,2*N-1))
    B = N*((k//N))
    #print(A,B,k//N,k,N)

    return A+B#+A//N


import numpy as np

s=input()
t=input()

td=list(set(t))

N=len(s)
d={}

import sys

R = set(list(s))
L = set(list(t))

if not(L <= R):
    print(-1)
    sys.exit()

for std in td:
    d[std] =[0]*(2*N)



for i in range(len(s)*2):
    #nd[s[i]]

    for std in td:            
        if s[i%N]==std:
            d[std][i]=1



dcs={}
for std in td:
    dcs[std]=np.cumsum(d[std])


last=-1
for ts in t:
    #print(last)
    last=next(ts,last+1)


print(last+1)


#print(dcs)
