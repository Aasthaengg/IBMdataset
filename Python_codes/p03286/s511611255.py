n = int(input())
s = ''
while n != 0:
    r = n % 2
    if r < 0:
        r += 2
    n = (n - r) // (-2)
    s += str(0 + r)
if s == '':
    print(0)
else:
    print(s[::-1])
