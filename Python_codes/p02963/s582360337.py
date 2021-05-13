s = int(input())
MOD = 10**9
y2, x2 = divmod(s, MOD)
if y2+1 <= MOD:
    x2 = abs(x2-MOD)
    y2 += 1
print(0, 0, 10**9, 1, x2, y2)
