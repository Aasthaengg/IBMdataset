def func(a):
    if a % 2 == 0:
        return a // 2
    else:
        return 3 * a + 1

s = int(input())
res = [s]
idx = 0
for i in range(2, 10 ** 6 + 1):
    s = func(s)
    if s in res:
        idx = i
        break
    res.append(s)
print(idx)