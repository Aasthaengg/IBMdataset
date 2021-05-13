N, L = map(int, input().split())

taste = [L + i for i in range(N)]
taste_abs = [abs(i) for i in taste]
min_index = taste_abs.index(min(taste_abs))
eat = taste[min_index]

print(sum(taste) - eat)
