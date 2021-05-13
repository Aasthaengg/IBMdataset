from itertools import permutations
res = float("inf")
for a, b, c in permutations(map(int, input().split()),3):
    res = min(abs(b-a) + abs(c-b),res)
print(res)