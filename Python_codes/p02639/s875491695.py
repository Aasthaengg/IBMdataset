import sys
lines = list(s.rstrip("\n") for s in sys.stdin)
numbers = list(map(int, lines[0].split(" ")))
for i, value in enumerate(numbers):
    if value == 0:
        print(i + 1)
        break
