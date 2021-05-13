N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

max_x = max(x + [X])
min_y = min(y + [Y])

print("War" if max_x >= min_y else "No War")