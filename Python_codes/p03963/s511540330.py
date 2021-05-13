n,k = map(int,input().split())
ans = [0]*n
ans[0] = k
for i in range(n-1):
    ans[i+1] = ans[i]*(k-1)
print(ans[-1])