N, M = map(int, input().split())
drinks = [list(map(int, input().split())) for _ in range(N)]

drinks.sort()

ans = 0
for i in range(N):
    if M < drinks[i][1]:
        ans += M * drinks[i][0]
        break
    else:
        ans += drinks[i][1] * drinks[i][0]
        M -= drinks[i][1]
print(ans)