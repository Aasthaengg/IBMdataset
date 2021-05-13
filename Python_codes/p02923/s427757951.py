N = int(input())
H = list(map(int, input().split()))
ans = 0
r = 0
for i in range(N-2, -1, -1):
    if H[i+1] <= H[i]:
        r += 1
        if r > ans:
            ans = r
    else:
        r = 0
print(ans)
