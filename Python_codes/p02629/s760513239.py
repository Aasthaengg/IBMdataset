a = int(input())
c = ''
while (a > 26):
    b = int(a) % 26
    c += chr(ord('a') + (25 if b == 0 else int(b) - 1))
    a = int(a / 26 - 1 if a % 26 == 0 else a / 26)
c += chr(ord('a') + int(a) - 1)
print(c[::-1])
