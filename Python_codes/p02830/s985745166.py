N = int(input())
S,T = map(str,input().split())
lsS = list(S)
lsT = list(T)
ans = ''
for i in range(N):
    ans += lsS[i]+lsT[i]
print(ans)