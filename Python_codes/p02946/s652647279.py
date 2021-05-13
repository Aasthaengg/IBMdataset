K, X = map(int, input().split())

min_index = X - K + 1
max_index = X + K

for i in range(min_index, max_index):
    print(i, end=" ")