import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n = int(lines.pop(0))
p_list = [int(n) for n in lines[0].split(" ")]

def _iter_minimum():
    prev = sys.maxsize
    for p in p_list:
        m = min(prev, p)
        yield m
        prev = m

mininum_list = list(_iter_minimum())

count = 0
for p, m in zip(p_list, mininum_list):
    if p == m:
        count += 1

print(count)
