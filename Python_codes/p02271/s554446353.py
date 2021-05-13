def solve(k, i):
    if k == 0: return True
    if i < n and min(A[i:]) <= k <= sum(A[i:]):
        r1 = solve(k-A[i], i+1)
        if r1: return r1
        r2 = solve(k, i+1)
        if r2: return r2
n = input()
A = map(int, raw_input().split())
q = input()
M = map(int, raw_input().split())
for k in M:
    print 'yes' if solve(k, 0) else 'no'