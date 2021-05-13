N = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
scores = [V[i] - C[i] for i in range(N)]

ans = 0
for score in scores:
    if score > 0:
        ans += score
print(ans)