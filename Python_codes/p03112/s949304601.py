a,b,q = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]
s.sort()
t.sort()
#print(s)
#print(t)
#print(x)
from bisect import bisect_left

def search_st(xi, s, t):
    ret = 10 ** 15
    ls = len(s)
    lt = len(t)
    ss = bisect_left(s, xi)
    si = s[ss % ls]
    st = bisect_left(t, si)
    ti = t[st % lt]
    ret = min(ret, abs(xi - si) + abs(si - ti))
    #print(si, ti, ret)
    st -= 1
    ti = t[st % lt]
    ret = min(ret, abs(xi - si) + abs(si - ti))
    #print(si, ti, ret)
    ss -= 1
    si = s[ss % ls]
    st = bisect_left(t, si)
    ti = t[st % lt]
    ret = min(ret, abs(xi - si) + abs(si - ti))
    #print(si, ti, ret)
    st -= 1
    ti = t[st % lt]
    ret = min(ret, abs(xi - si) + abs(si - ti))
    #print(si, ti, ret)
    return ret

for i in range(q):
    xi = x[i]
    ans = 10 ** 15
    # sから先
    ans = min(ans, search_st(xi, s, t))
    ans = min(ans, search_st(xi, t, s))
    print(ans)
