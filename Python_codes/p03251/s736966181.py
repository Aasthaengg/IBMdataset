_, _, x, y = map(int, input().split())
X = list(map(int, input().split())) + [x]
Y = list(map(int, input().split())) + [y]
print("No War" if min(Y) - max(X) > 0 else "War")