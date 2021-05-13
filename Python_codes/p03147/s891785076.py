n = int(input())
h = list(map(int, input().split()))

ans = 0
active = 0

for i in range(n):
    if h[i] >= active:
        ans += h[i] - active
        active = h[i]
    else:
        active = h[i]
print(ans)