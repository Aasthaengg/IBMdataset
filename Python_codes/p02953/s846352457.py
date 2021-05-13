n = int(input())
h = list(map(int,input().split()))

ans = "Yes"
t = h[0]
for i in range(1,n):
    t = max(h[i-1],t)
    if h[i] - t <= -2:
        ans = "No"
        break

print(ans)
