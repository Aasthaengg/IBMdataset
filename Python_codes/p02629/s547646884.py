n = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = ''

while n != 0:
    n -= 1
    n,mod = divmod(n, 26)
    ans += alphabet[mod]
print(ans[::-1])