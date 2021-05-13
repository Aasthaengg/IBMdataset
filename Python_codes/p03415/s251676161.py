L = list(input() for _ in range(3))
res = []
for i in range(3):
    res.append(L[i][i])
print("".join(res))