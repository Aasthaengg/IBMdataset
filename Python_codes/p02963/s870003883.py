s = int(input())

t = [0, 0, 10 ** 9, 1, None, None]
t[5] = (s + 10 ** 9 - 1) // 10 ** 9
t[4] = (10 ** 9 * t[5]) - s

print(*t)