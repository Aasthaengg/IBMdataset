import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip().split()
hina = set()
for s in S:
    hina.add(s)

print("Three" if len(hina) == 3 else "Four")