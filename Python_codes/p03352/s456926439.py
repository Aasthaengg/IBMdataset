X = int(input())
ans = 0

for i in range(2, X):
    for j in range(1, X):
        if j**i > X:
            break
        else:
            ans = max(ans, j**i)
if X == 1:
    print(1)
else:
    print(ans)
