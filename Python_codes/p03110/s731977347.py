n = int(input())
xu = []
ans = []
for i in range(n):
    XU = list(input().split())
    xu.append(XU)
for m, c in xu:
    if c == "JPY":
        ans.append(int(m))
    else:
        ans.append(float(m)*380000)
print(sum(ans))