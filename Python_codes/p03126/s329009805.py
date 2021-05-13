n, m = map(int, input().split())
foods = [0 for _ in range(m + 1)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(1, a[0] + 1):
        foods[a[j]] += 1
print(foods.count(n))