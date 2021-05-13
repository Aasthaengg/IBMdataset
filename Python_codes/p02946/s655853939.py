K, X = map(int, input().split())
array = []

for x in range(X - K + 1, X + K, 1):
    array.append(str(x))
print(" ".join(array))
