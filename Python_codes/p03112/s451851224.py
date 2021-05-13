#template
def inputlist(): return [int(k) for k in input().split()]
def intinput(): return int(input())
#template
A,B,Q = inputlist()
s = [0]*A
t = [0]*B
x = [0]*Q
for i in range(A):
    s[i] = intinput()
for i in range(B):
    t[i] = int(input())
for i in range(Q):
    x[i] = intinput()
s.sort()
t.sort()
ans = [0]*Q
from bisect import bisect_left
for i in range(Q):
    xa = x[i]
    s0,s1 = -1,10**18+1
    t0,t1 = -1,10**18+1
    index_s = bisect_left(s,xa)
    index_t = bisect_left(t,xa)
    if index_s == 0:
        s1 = s[0]
    if index_t == 0:
        t1 = t[0]
    if index_s == A:
        s0 = s[-1]
    if index_t == B:
        t0 = t[-1]
    if index_s != 0 and index_s != A:
        s0 = s[index_s-1]
        s1 = s[index_s]
    if index_t != 0 and index_t != B:
        t0 = t[index_t-1]
        t1 = t[index_t]
    if s0 == -1 or t1 == 10**18+1:
        d1 = 10**18+1
        d2 = 10**18+1
    if s0 != -1 and t1 != 10**18+1:
        d1 = (xa-s0)*2+(t1-xa)
        d2 = (t1-xa)*2+(xa-s0)
    if t0 == -1 or s1 == 10**18+1:
        d3 = 10**18+1
        d4 = 10**18+1
    if t0 != -1 and s1 != 10**18+1:
        d3 = (xa-t0)*2+(s1-xa)
        d4 = (s1-xa)*2+(xa-t0)
    m1 = min(s0,t0)
    M1 = max(s1,t1)
    if m1 == -1:
        d5 = 10**18+1
    if m1 != -1:
        d5 = abs(xa-m1)
    if M1 == 10**18+1:
        d6 = 10**18+1
    if M1 != 10**18+1:
        d6 = abs(xa-M1)
    ans[i] = min(d1,d2,d3,d4,d5,d6)
for i in range(Q):
    print(ans[i])
