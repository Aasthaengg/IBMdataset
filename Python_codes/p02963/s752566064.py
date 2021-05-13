S = int(input())

l = [0,0]
if S <= 10 ** 9:
    a = [S, 0, 0, 1]
else:
    u = S // 10 ** 9
    if S % 10 ** 9 != 0:
        u += 1
    d = u * (10 ** 9) - S
    a = [u, d, 1, 10 ** 9]
l.extend(a)
print(" ".join(map(str, l)))