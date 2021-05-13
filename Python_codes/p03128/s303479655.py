import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
d = [None,2,5,5,4,5,6,3,7,6]
ds = [(i, d[i]) for i in a] # (数、本数)
ds.sort(reverse=True)

dp = [list(0 for _ in range(m+1)) for _ in range(n+1)]
for i in range(1, n+1):
    for j,(ii,num) in enumerate(ds):
        if i-num==0 or (i-num>0 and dp[i-num][0]>0):
            item = dp[i-num][:]
            item[0] += 1
            item[j+1] += 1
#             print(item)
            dp[i] = max(dp[i], item)
ans = ""
for i,item in enumerate(dp[n][1:]):
    ans += str(ds[i][0])*item
print(ans)
