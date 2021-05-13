X = int(input())
A = list(map(int, [input() for i in range(X)]))
A = list(set(A))
print(len(A))