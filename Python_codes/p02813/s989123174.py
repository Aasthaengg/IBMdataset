from itertools import permutations

n = int(input())
x, y = tuple(map(int, input().split())), tuple(map(int, input().split()))
p = [per for per in permutations(list(range(1, n+1)), n)]
print(abs(p.index(x) - p.index(y)))