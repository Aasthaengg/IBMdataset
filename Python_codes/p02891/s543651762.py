from collections import Counter
def dd(S):
    S += "#"
    s0 = S[0]
    cnt, r = 1, 0
    for s in S[1:]:
        if s == s0:
            cnt += 1
        else:
            r += cnt // 2
            cnt = 1
        s0 = s
    return r
S = input().rstrip()
K = int(input())
s = dd(S)
t = dd(S*2)
if len(Counter(S))==1:
    print(len(S)*K//2)
else:
    print(s*K + (t-2*s)*(K-1))
"""
aaa
3
"""