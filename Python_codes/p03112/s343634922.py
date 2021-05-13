import sys
input = sys.stdin.readline
A, B, Q = map(int, input().split())
inf = 10**18
S = [-inf]
for _ in range(A):
    S.append(int(input()))
S.append(inf)
T = [-inf]
for _ in range(B):
    T.append(int(input()))
T.append(inf)
def f_s(x, l):
    mn, mx = -1, len(l)
    idx = mx//2
    while mx-mn>1:
        if l[idx] < x:
            idx, mn = (idx + mx)//2, idx
            continue
        idx, mx = (idx + mn)//2, idx
    return idx

for _ in range(Q):
    q = int(input())
    xi, yi = f_s(q, S), f_s(q, T)
    s1, s2 = S[xi], S[xi+1]
    t1, t2 = T[yi], T[yi+1]
    print(min([
        max(q-s1,q-t1),
        max(s2-q, t2-q),
        2*(s2-q) + q-t1,
        2*(t2-q) + q-s1,
        2*(q-s1) + t2-q,
        2*(q-t1) + s2-q,
        ]))
#    print(q, s1, s2, t1, t2)

#    print(S[xi], T[yi])
