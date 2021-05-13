n = int(raw_input())
A = map(int, raw_input().split())
q = int(raw_input())
m = map(int, raw_input().split())

def solve(i, m):
    if m == 0:
        return 1
    if i >= n or m > sum(A):
        return 0
    res = solve(i + 1, m) or solve(i + 1, m - A[i])
    return res
        
for j in range(0, q):
    if solve(0, m[j]):
        print "yes"
    else:
        print "no"