# みんなのプロコン 2019: A – Anti-Adjacency
n, k = [int(s) for s in input().split()]
print('YES' if k * 2 - 1 <= n else 'NO')