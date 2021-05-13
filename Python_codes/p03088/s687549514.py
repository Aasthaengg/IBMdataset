#賢く解くと...
n=int(input())
mod=10**9+7
memo=[{} for _ in range(n+1)]

def judge(last4):
    for i in range(4):
        t=list(last4)
        if i<3:
            t[i],t[i+1]=t[i+1],t[i]
        s=''.join(t)
        if 'AGC' in s:
            return False
    return True

def dfs(i,last3):
    if last3 in memo[i]:
        return memo[i][last3]
    if i==n:
        return 1
    res=0
    for c in 'ACGT':
        if judge(last3+c):
            res=(res+dfs(i+1,last3[1:]+c))%mod
    memo[i][last3]=res
    return res

print(dfs(0,'TTT'))