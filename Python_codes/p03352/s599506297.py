X = int(input())
ans = 0
for b in range(1, 1001):
    for p in range(2, 1001):
        if b**p <= X:
            if b**p > ans:
                ans = b**p
        else:
            break

print(ans)