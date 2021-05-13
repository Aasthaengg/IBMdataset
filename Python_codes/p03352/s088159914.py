X = int(input())

M = int(X**.5) + 1

ans = 1

for i in range (2, M):
    for j in range(2, 10):
        if X < i**(j+1):
            ans = max(ans, i**j)
            break

print(ans)