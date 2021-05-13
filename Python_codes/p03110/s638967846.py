n = int(input())
x = [0]*n
ans = 0
for i in range(n):
    x = list(map(str,input().split()))
    if x[1] == "BTC":
        ans += float(x[0])*380000
    else:
        ans += float(x[0])
print(ans)