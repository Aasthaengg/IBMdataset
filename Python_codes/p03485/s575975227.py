import sys

a, b = [int(x) for x in sys.stdin.readline().strip().split(" ")]
if (a + b) % 2 == 1:
    print((a + b + 1) // 2)
else:
    print((a + b) // 2)
