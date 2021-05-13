N=int(input())
S,T=map(str, input().split())
ans = ''
for i, j in zip(S,T):
    ans += i + j
print(ans)