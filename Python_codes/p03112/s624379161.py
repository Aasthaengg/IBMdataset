import sys
input=sys.stdin.readline
a, b, q = map(int, input().split())
s = []
t = []
x = []
for i in range(a):
    s.append(int(input()))
for i in range(b):
    t.append(int(input()))
for i in range(q):
    x.append(int(input()))
import bisect
def get(x):
    ls,rs,lt,rt=10**13,10**13,10**13,10**13
    s_ind = bisect.bisect_left(s,x)
    t_ind = bisect.bisect_left(t,x)
    if s_ind!=0:
        ls=abs(x - s[s_ind-1])
    if s_ind!=a:
        rs=abs(x - s[s_ind])
    if t_ind!=0:
        lt=abs(x - t[t_ind-1])
    if t_ind!=b:
        rt=abs(x - t[t_ind])
    return ls,rs,lt,rt

for que in x:
    ls,rs,lt,rt = get(que)

    rr = max(rs,rt)
    ll = max(ls,lt)
    lsrt = 2*ls+rt
    ltrs = 2*lt+rs
    rslt = 2*rs+lt
    rtls = 2*rt+ls
    ans = min([rr,ll,lsrt,ltrs,rslt,rtls])
    print(ans)