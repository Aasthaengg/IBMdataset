X, Y = map(int, input().split())

now = X
res = 0
for i in range(10 ** 9):
    res += 1
    now *= 2
    if now > Y:
        break

print(res)
