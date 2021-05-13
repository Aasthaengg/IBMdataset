def dfs(n):
    global t
    S[n] = t
    DP[n]=1
    for i in A[n][2:]:
        if not DP[i]:
            t += 1
            dfs(i)
    t += 1
    F[n] = t
n = int(input())
A = [0]*(n+1)
S = [0]*(n+1)
F = [0]*(n+1)
DP = [0]*(n+1)
for i in range(n):
    A[i+1] = [int(i) for i in input().split()]
t = 0
for i in range(1,n+1):
    if not DP[i]:
        t+=1
        dfs(i)
for i in range(1,n+1):
    tmp = "{} {} {}".format(i,S[i],F[i])
    print(tmp)
