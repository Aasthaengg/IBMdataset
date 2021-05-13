n = int(input())
x, u = [0]*n, [0]*n

for i in range(n):
    x[i], u[i] = map(str, input().split())
    x[i] = float(x[i])
ans = 0
for i in range(n):
    if u[i] == "JPY":
        ans += int(x[i])
    else:
        ans += x[i]*380000
print(ans)
