import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
s = set()
for _ in range(N):
    s.add(I())

print(len(s))
