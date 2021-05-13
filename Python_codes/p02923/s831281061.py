N = int(input())
H = tuple(map(int, input().split()))

ans = 0
d = 0
for i in range(N - 1):
    if H[i+1] <= H[i]:
        d += 1
        ans = max(ans, d)
    else:
        d = 0
print(ans)