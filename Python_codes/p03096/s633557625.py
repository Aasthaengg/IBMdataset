def int_raw():
    return int(raw_input())

def ss_raw():
    return raw_input().split()

def ints_raw():
    return map(int,ss_raw())

INF = 1<<29

DIV = 10**9+7

def make2d_arr(w,h,val =INF):
    return [[val]*w for i in xrange(h)]

def floyd_warshall(costs):
    N = len(costs)
    for k in xrange(N):
        for i in xrange(N):
            for j in xrange(N):
                costs[i][j]  = min(costs[i][j],costs[i][k]+costs[k][j])
    return costs

N = int_raw()
C =[]
dp = [0 for i in xrange(N)]

m_prev = {}
prevs = [-1 for i in xrange(N)]

for i in xrange(N):
    c = int_raw()
    C.append(c)
    if c in m_prev:
        prevs[i] = m_prev[c]
        m_prev[c]= i
    else:
        m_prev[c]=i
    
dp[0] =1

for x in xrange(1,N):
    cx = C[x]
    dp[x] = dp[x-1]
    if cx == C[x-1]:
        continue
    y = prevs[x]
    if y != -1:
        dp[x]+=dp[y]
        dp[x]= dp[x]%DIV        
    """for y in xrange(x-2,-1,-1):
        cy = C[y]
        if cx == cy:
            dp[x]+=dp[y]
            dp[x]= dp[x]%DIV
            break"""

print dp[-1] 



