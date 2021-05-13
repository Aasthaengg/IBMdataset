import sys
N = int(input())
x = set()
for _ in range(N):
    s = sys.stdin.readline()
    x.add(s)
print(len(x))