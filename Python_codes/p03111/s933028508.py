import itertools
N, A, B, C = map(int, input().split())
L = [int(input()) for i in range(N)]
ans = float('inf')
for bit in itertools.product(range(4), repeat=N):
    ABC = [0]*3
    cost = 0
    for i, abc in enumerate(bit):
        if abc == 3:
            continue
        ABC[abc] += L[i]
        if ABC[abc] != L[i]:
            cost += 10
    if 0 in ABC:
        continue
    cost += abs(ABC[0] - A) + abs(ABC[1] - B) + abs(ABC[2] - C)
    ans = min(ans, cost)
print(ans)
