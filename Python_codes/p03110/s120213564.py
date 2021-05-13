N = int(input())
moneies = [input().split() for i in range(N)]

ans = 0
for money in moneies:
    if money[1] == "JPY":
        ans += int(money[0])
    else:
        ans += float(money[0]) * 380000
print(ans)