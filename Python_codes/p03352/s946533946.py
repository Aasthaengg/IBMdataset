X = int(input())

res = 1
for i in range(X):
    for p in range(2, X):
        if i ** p <= X:
            res = max(res, i ** p)
        else:
            break
print(res)
