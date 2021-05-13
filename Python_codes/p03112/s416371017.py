import sys
input = sys.stdin.buffer.readline

a, b, q = map(int, input().split())
S = [0]*a
T = [0]*b
for i in range(a):
    s = int(input())
    S[i] = s
for i in range(b):
    t = int(input())
    T[i] = t

S.sort()
T.sort()
S = [-10**18]+S+[10**18]
T = [-10**18]+T+[10**18]
import bisect
for i in range(q):
    x = int(input())
    ans = 10**18
    ids = bisect.bisect_right(S, x)
    idt = bisect.bisect_right(T, x)
    for ks in (-1, 0):
        for kt in (-1, 0):
            s = S[ids+ks]
            t = T[idt+kt]
            temp = min(abs(s-x)+abs(s-t), abs(t-x)+abs(s-t))
            ans = min(ans, temp)
    print(ans)