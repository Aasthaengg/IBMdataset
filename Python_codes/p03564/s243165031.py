N = int(input())
K = int(input())

ans = 1

for i in range(N):
    if ans*2<=ans+K:
        ans *=2
    elif ans*2>ans+K:
        ans+=K
print(ans)