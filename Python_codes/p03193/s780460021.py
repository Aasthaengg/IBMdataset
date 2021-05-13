N, H, W = tuple(map(int, input().split()))
ans = 0
for i in range(N):
    a, b = tuple(map(int, input().split()))
    if H <= a and W <= b:
        ans += 1
print(ans)