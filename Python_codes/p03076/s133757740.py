import itertools

foods = [int(input()) for _ in range(5)]
all_route = list(itertools.permutations(foods))
ans = []
for route in all_route:
    total = 0

    for i in range(len(route) - 1):
        total += route[i]
        if route[i] % 10 != 0:
            total += 10 - route[i] % 10
    total += route[-1]
    ans.append(total)
print(min(ans))
