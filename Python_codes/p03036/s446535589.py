import sys

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


r, d, x = nm()
for i in range(10):
    x = r * x - d
    print(x)
