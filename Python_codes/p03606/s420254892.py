N = int(input())
LR = [tuple(map(int,input().split())) for i in range(N)]
ans = 0
for l,r in LR:
    ans += r-l+1
print(ans)