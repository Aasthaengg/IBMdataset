A,B,C,K = map(int, input().split())
ans = 0
ans += min(A,K)
K -= A+B
if(K>0):
    ans -= min(C,K)
print(ans)