n = int(input())
ans = 0
for i in range(n):
    x = list(map(str,input().split()))
    if x[1] == "JPY":
        ans += int(x[0])
    else:
        ans += float(x[0])*380000
print(ans)