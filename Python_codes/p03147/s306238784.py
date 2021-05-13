
N = int(input())
X = list(map(int, input().split()))

res = 0
for _ in range(100):
    if all(v == 0 for v in X):
        break

    flag = False
    for i in range(N):
        if X[i] > 0:
            X[i] -= 1
            flag = True
        elif flag:
            flag = False
            res += 1

    if flag:
        res += 1

print(res)
