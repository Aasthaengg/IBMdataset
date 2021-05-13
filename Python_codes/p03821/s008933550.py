n = int(input())
cnt = 0
ab_l = [list(map(int, input().split())) for _ in range(n)]
for ab in ab_l[::-1]:
    a, b = ab[0], ab[1]
    a += cnt
    if a % b != 0:
        cnt += b - a%b
print(cnt)