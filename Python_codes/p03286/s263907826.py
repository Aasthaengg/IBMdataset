n = int(input())

s = ""

while n != 0:
    r = n % 2
    s += "0" if r == 0 else "1"
    n = (n - r) // (-2)

if len(s) > 0:
    print(s[::-1])
else:
    print(0)