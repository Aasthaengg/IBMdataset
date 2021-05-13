import sys

lines = [line for line in sys.stdin]

n = int(lines[0])
s = list(map(int,lines[1].split()))
s.reverse()
s=map(str,s)
print(" ".join(s))