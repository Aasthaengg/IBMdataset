N,P = map(int,input().split())
S = map(int,input())
S_li = [0]*(N+1)
S_rev = reversed(tuple(S))

tmp = 0
count= 0
from  collections import Counter

if 10%P==0:
    counter = 0
    for i,num in enumerate(S_rev):
        if num%P==0:
            counter += N-i
    print(counter)

else:
    ctr = [0] * P
    ctr[0] = 1
    ret = 0
    t = 0
    c = 1
    for x in S_rev:
        t = (t + c * x) % P
        ret += ctr[t]
        ctr[t] += 1
        c = c * 10 % P
 
    print(ret)
