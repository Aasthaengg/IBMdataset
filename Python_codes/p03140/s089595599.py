n = int(input())
abc = [list(input()) for _ in range(3)]
ans = 2 * n
for j in range(n):
    x = 0
    for i in range(3):
        if abc[i][j] == abc[(i + 1) % 3][j]:
            x += 1
        if x >= 2:
            break
    ans -= x
print(ans)