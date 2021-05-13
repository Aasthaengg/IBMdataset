import sys
a, b, c = map(int, input().split())

if a == b and b == c:
    print(-1 if a % 2 == 0 else 0)
    sys.exit(0)

i = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    a, b, c = (b + c) / 2, (c + a) / 2, (a + b) / 2
    i += 1

print(i)
