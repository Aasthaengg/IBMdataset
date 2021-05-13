n=int(input())
h = list(map(int,input().split())) + [0]
th = 0
ans = 0
for i in range(n+1):
    if h[i] > th:
        th = h[i]
    elif h[i] < th:
        ans += th-h[i]
        th = h[i]
print(ans)