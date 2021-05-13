MOD = 10**9+7
N = int(input())
C = []
C.append(int(input()))
for i in range(N-1):
    c = int(input())
    if c == C[-1]:
        continue
    C.append(c)
#print(C)
N = len(C)
lis = [[0] for i in range(max(C)+1)]
for i in range(N):
    lis[C[i]].append(i+1)
for i in range(len(lis)):
    lis[i].append(MOD)

def binary_search(lis,i):
    ok = 0
    ng = len(lis)-1
    while ng-ok > 1:
        mid = (ok + ng)// 2
        if lis[mid] < i:
            ok = mid
        else:
            ng = mid
    return lis[ok]
#print(binary_search([0,1,2,3,4],3))
#print(lis)
dp = [0] * (N+1)
dp[0] = 1
for i in range(1,N+1):
    dp[i] += dp[i-1]
    p = binary_search(lis[C[i-1]],i)
    if p != 0:
        dp[i] += dp[p]
    dp[i] %= MOD
    #print(p)
print(dp[-1])
