L, R = map(int, input().split())
mod = 2019

if R - L >= 2019:
    print(0)
    exit()

L %= 2019
R %= 2019

ans = 2019
for i in range(min(L, R), max(L, R)+1):
    for j in range(i+1, max(L, R)+1):
        ans = min(ans, (i*j)%mod)

print(ans)
