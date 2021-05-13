n = input()
digit = len(n)
n = int(n)
ans = (digit - 1) * 9 + n // (10 ** (digit - 1)) - 1
tmp = n - n // (10 ** (digit - 1)) * (10 ** (digit - 1))
if tmp == (10 ** (digit - 1)) - 1:
    ans += 1
print(ans)