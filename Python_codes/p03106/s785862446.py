import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
a, b, k = [int(num) for num in lines.pop(0).split(" ")]
count = 0
for n in range(min(a, b), 0, -1):
    if (a % n == 0) and (b % n == 0):
        count += 1
    if count == k:
        break
print(n)
