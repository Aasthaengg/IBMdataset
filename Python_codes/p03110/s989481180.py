N = int(input())
ans = 0
for i in range(N):
    x,u = list(input().split())
    if u == 'JPY':
        ans += float(x)
    else:
        ans += float(x)*3.8*10**5
print(ans)
