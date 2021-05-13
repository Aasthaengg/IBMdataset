cost = 0
n = int(input())
for _ in [0] * n:
    s = input().split()
    x, u = float(s[0]), s[1]
    if u == "BTC":
        cost += x * 38e4
    else:
        cost += x
print(cost)