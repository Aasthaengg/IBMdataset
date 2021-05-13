import sys
readline = sys.stdin.readline
readline()
bits = 1
for a in map(int, readline().split()): bits |= bits << a
readline()
sys.stdout.write("\n".join("yes"*((bits >> q) & 1)or"no" for q in map(int, readline().split())))
sys.stdout.write("\n")