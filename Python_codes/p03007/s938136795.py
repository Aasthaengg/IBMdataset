N = int(input())
*A, = map(int, input().split())
INF = 10**9
p = q = 0
for i, a in enumerate(A):
    if a > 0:
        p += 1
    elif a < 0:
        q += 1

def solve(s, t):
    R = []
    i = A.index(s)
    if s == t:
        j = A.index(t, i+1)
    else:
        j = A.index(t)
    for k, a in enumerate(A):
        if i == k or j == k:
            continue
        if a >= 0:
            R.append("%d %d\n" % (s, a))
            s -= a
    for k, a in enumerate(A):
        if i == k or j == k:
            continue
        if a < 0:
            R.append("%d %d\n" % (t, a))
            t -= a
    R.append("%d %d\n" % (t, s))
    t -= s
    return t, R
ans = 0
if p > 0 and q > 0:
    s = t = 0
    for a in A:
        if a > 0:
            t = a
        elif a < 0:
            s = a
    ans, R = solve(s, t)
elif p > 0:
    A.sort()
    ans, R = solve(A[0], A[1])
elif q > 0:
    A.sort()
    ans, R = solve(A[-2], A[-1])
else:
    R = ["0 0\n"]*(N-1)
print(ans)
print("".join(R))