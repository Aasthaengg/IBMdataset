n = int(input())
ans = 0
a = 0,1
for i in range(n):
    a,b = input().split()
    if b == "BTC":
        a = float(a)*380000
        ans += a
    else:
        ans += int(a)
print(ans)