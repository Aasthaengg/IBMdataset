S = int(input())

if S != 10 ** 18:
    q = S // 10 ** 9 + 1
    r = 10 ** 9 * q - S
else:
    q = S // 10 ** 9
    r = 10 ** 9 * q - S

print(0, 0, q, r, 1, 10 ** 9)