
        
def solve(i,m):
    if dp[i][m] != -1:
        return dp[i][m]
    if m == 0:
        dp[i][m] = True
    elif i >= n:
        dp[i][m] = False
    elif solve(i+1, m):
        dp[i][m] = True
    elif solve(i+1, m-a[i]):
        dp[i][m] = True
    else:
        dp[i][m] = False
    return dp[i][m]

n = input()
a = map(int,raw_input().split())
q = input()
p = map(int,raw_input().split())
dp = [[-1 for i in xrange(2001)] for j in xrange(21)]
for i in xrange(q):
    if solve(0,p[i]):
        print "yes"
    else:
        print "no"