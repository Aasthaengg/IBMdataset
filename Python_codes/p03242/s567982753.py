import sys

rr = lambda: sys.stdin.readline().rstrip()
print(rr().translate(str.maketrans('19', '91')))