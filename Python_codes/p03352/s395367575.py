X = int(input())

if X == 1:
    print(1)
    exit()

ans = [False] * (X + 1)
for i in range(2, X + 1):
    v = i * i
    while v <= X:
        ans[v] = True
        v *= i

for i in range(X, -1, -1):
    if ans[i]:
        print(i)
        exit()
