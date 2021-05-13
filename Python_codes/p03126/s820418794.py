n, m = map(int, input().split())
foods = [0] * (m + 1)
for i in range(n):
    k, *a = map(int, input().split())
    for j in a:
        foods[j] += 1

print(foods.count(n))