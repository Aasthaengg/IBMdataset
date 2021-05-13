n,m = map(int,input().split())
ans = [1] + [1]*n
if n == 1:
    print(1)
    exit()
for i in range(m):
    ans[int(input())] = 0
for i in range(n-2,-1,-1):
    if ans[i] == 0:
        continue
    ans[i] = (ans[i+1] + ans[i+2])%1000000007
print(ans[0])