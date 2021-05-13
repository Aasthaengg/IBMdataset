import sys
import collections
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, m = [int(num) for num in lines.pop(0).split(" ")]
def iter_a_set():
    for line in lines:
        fs = [int(num) for num in line.split(" ")]
        k = fs.pop(0)
        yield set(fs)
foods = set(range(1, m + 1))
for a_set in iter_a_set():
    foods &= a_set
print(len(foods))
