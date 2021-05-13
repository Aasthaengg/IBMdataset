N = int(input())
res = 0
for i in range(N):
    x,u = map(str, input().split())
    if u == "JPY":
        res += int(x)
    else:
        res += float(x)*380000
print(res)