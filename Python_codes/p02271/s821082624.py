n = int(raw_input())
A = map(int, raw_input().strip().split(' '))
q = int(raw_input())
M = map(int, raw_input().strip().split(' '))

memo = []
for i in range(len(A)+1):
    memo.append([None]*2000)

def solve(i,m):
    if memo[i][m] != None: return memo[i][m]
    if m == 0:
        memo[i][m] = True
        return True
    elif i >= n:
        memo[i][m] = False
        return False
    else:
        ret = solve(i+1,m) | solve(i+1,m-A[i])
        memo[i][m] = ret
        return ret

for m in M:
    if solve(0,m): print "yes"
    else: print "no"