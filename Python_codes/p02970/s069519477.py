n, d = map(int, input().split())

num, mod = divmod(n, 2 * d + 1)
if mod == 0:
    print(num)
else:
    print(num + 1)