N = int(input())
XU = [list(map(str,input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    if XU[i][1] == "JPY":
        ans += float(XU[i][0])
    else:
        ans += 380000*float(XU[i][0])

print(float(ans))