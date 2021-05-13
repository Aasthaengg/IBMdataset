n = int(input())
h = list(map(int, input().split()))
h.append(0)

ans = 0
x = 0
for i in range(1,n+1):
    if h[i] < h[i-1]:
        ans += h[i-1] - x
        x = h[i]
print(ans)  