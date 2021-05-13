import sys
s = sys.stdin.readline().strip()
print(sum([a-b for a, b in zip(list(range(s.count('W'), len(s))), [i for i, c in enumerate(s) if c == 'B'])]))