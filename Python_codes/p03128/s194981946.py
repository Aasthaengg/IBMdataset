from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)


n,m = inm()
a = inl()
a.sort()
cs = [0,2,5,5,4,5,6,3,7,6]
dp = [-1]*(n+9)
dp[0] = 0
for i in range(n):
    if dp[i]>=0:
        for x in a:
            c = cs[x]
            dp[i+c] = max(dp[i+c], dp[i]+1)
ans = []
t = n
k = dp[n]
for j in range(k,0,-1):
    for i in range(m-1,-1,-1):
        x = a[i]
        c = cs[x]
        if t>=c and dp[t-c]==j-1:
            ans.append(str(x))
            t -= c
            break
print(''.join(ans))
