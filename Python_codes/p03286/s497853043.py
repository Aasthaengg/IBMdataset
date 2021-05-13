import sys

n = int(input())

if n == 0:
    print(0)
    sys.exit()

cur = n
S = ""

while cur != 0:
    if cur % 2 == 0:
        S = "0" + S
        cur /= -2
    else:
        S = "1" + S
        cur -= 1
        cur /= -2
print(S)
