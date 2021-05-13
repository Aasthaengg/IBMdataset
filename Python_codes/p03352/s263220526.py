X = int(input())
res = 0
for i in range(1, 1000):
    for j in range(2, 1000):
        if i**j <= X:
            res = max(i**j, res)
        else:
            break
print(res)