n, m, x, y = map(int, input().split())
X = sorted(list(map(int, input().split()))+[x])[-1]
Y = sorted(list(map(int, input().split()))+[y])[0]
print('No War' if Y-X >= 1 else 'War')