n,m = map(int,input().split())
a = [int(input()) for _ in range(m)]

p = 10**9 +7
ans = [0]*(n+1)
ans[0] = 1
ans[1] = 1

broken = [0]*(n+1)
for i in a:
    broken[i]= -1

for i in range(1,n):
    if broken[i] == -1:
        ans[i] = 0
        ans[i+1] = ans[i-1]%p
    else:
        ans[i+1] = (ans[i-1] + ans[i])%p

print(ans[-1])