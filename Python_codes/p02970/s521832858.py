a, b = map(int, input().split())

ret = a // (b * 2 + 1)

if a % (b * 2 + 1) != 0:
    ret += 1

print(ret)
