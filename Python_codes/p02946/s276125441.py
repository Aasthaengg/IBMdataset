import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
k, x = [int(num) for num in lines.pop(0).split(" ")]
lis = [str(n) for n in range(x - k + 1, x + k)]
print(" ".join(lis))
