import sys

[A, B] = [int(x) for x in sys.stdin.readline().split(" ")]
sum = A + B
if sum % 2 == 0:
    print(int(sum / 2))
else:
    print("IMPOSSIBLE")
