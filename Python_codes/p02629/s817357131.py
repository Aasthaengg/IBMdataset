n = int(input())

ans = ''

while n > 0:
    n -= 1
    n, mod = divmod(n, 26)
    ans += chr(ord('a') + mod)

ans = ans[::-1]
print(ans)