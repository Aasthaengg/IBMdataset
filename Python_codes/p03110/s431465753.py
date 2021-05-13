N = int(input())
cost = []
yen = []
for i in range(N):
    n, a = input().split()
    cost.append(float(n))
    yen.append(a)
ans = 0
for i in range(N):
    if yen[i] == "JPY":
        ans += cost[i]
    else:
        ans += cost[i] * 380000
print(ans)