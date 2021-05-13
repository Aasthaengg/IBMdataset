def calc(n, x):
    result = 0
    for i in range(3, n + 1):
        for j in range(2, i):
            if i + j < x < i + 2 * j:
                result += 1
    return str(result)

ans = []
while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    ans.append(calc(n, x))

print("\n".join(ans))
