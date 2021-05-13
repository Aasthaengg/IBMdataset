def f(a, b):
    if a % 2 == 0:
        pass
    else:
        a -= 1
    a //= 2
    b += a
    return a, b

inp = list(map (int, input().split()))

cnt = 1
for i in range(inp[2]):
    if cnt % 2 == 0:
        inp[0], inp[1] = f(inp[1], inp[0])
    else:
        inp[1], inp[0] = f(inp[0], inp[1])


if inp[2] % 2 == 0:
    print(inp[0], inp[1], sep=" ")
else:
    print(inp[1], inp[0], sep=" ")