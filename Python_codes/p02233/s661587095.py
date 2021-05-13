import sys
n = int(input())
if n < 2:
    print(1)
    sys.exit()
a, b = 1, 1
for i in range(n-1):
    c = a + b
    a = b
    b = c
print(c)
