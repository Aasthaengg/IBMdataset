n = int(input())

ret = n // 11 * 2

if n % 11 == 0:
    pass
elif (n % 11) <= 6:
    ret += 1
else:
    ret += 2

print(ret)
