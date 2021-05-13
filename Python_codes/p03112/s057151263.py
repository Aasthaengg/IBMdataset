from bisect import bisect_left as bl
def dist(p1,p2): return abs(p1-p2)
INF = 10**18
a,b,q = map(int,input().split())
S = [-INF]+[int(input()) for _ in range(a)]+[INF]
T = [-INF]+[int(input()) for _ in range(b)]+[INF]
X = [int(input()) for _ in range(q)]

for i in range(q):
    ans = INF
    s = bl(S,X[i])
    t = bl(T,X[i])
    p = ((s,t),(s-1,t-1))
    for ps,pt in p:
        if dist(X[i],S[ps]) < dist(X[i],T[pt]):
            pt = bl(T,S[ps])
            ans = min(ans , dist(X[i],S[ps])+min(dist(S[ps],T[pt]),dist(S[ps],T[pt-1])))
        else:
            ps = bl(S,T[pt])
            ans = min(ans , dist(X[i],T[pt])+min(dist(T[pt],S[ps]),dist(T[pt],S[ps-1])))
    print(ans)