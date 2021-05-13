X = int(input())
ans = [False] * (X+1)
ans[1] = True
for i in range(2, X):
    for j in range(2, X):
        if i**j <= X:
            ans[i**j] = True
        else:
            break
for i in range(X, 0, -1):
    if ans[i]:
        print(i)
        break
