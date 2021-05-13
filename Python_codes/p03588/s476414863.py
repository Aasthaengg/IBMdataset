N = int(input())
amax, score = 0, 0
for _ in range(N):
    a, b = map(int, input().split())
    if amax < a:
        amax = a
        score = b
ans = amax + score
print(ans)