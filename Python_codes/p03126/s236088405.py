n, m = map(int, input().split())
ansers = [list(map(int, input().split())) for _ in range(n)]
foods = [0] * (m + 1)

for i in range(n):
    for j in range(1, len(ansers[i])):
        foods[ansers[i][j]] += 1

print(foods.count(n))
