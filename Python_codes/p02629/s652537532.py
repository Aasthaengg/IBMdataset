n = int(input())

abc = 'abcdefghijklmnopqrstuvwxyz'
s = ''
while n > 0:
    n -= 1
    n, mod = divmod(n, 26)
    s += abc[mod]
print(s[::-1])