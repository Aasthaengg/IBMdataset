s = int(input())

div, mod = divmod(s, 10 ** 9)
ans = [0, 0, 10 ** 9, 1]
ans += [(10 ** 9 - mod) * (mod != 0), div + (mod != 0)]
print(*ans)
