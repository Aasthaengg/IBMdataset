K, X = map(int, input().split())
lst = []
for i in range(X - (K - 1), X + K):
    lst.append(i)

print(*lst)
