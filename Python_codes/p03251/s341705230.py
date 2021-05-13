N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
print('War' if X >= min(y) or Y <= max(x) or max(x) >= min(y) else 'No War')
