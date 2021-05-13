import sys

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


a, b = nm()
if a >= 13:
    print(b)
elif 6 <= a <= 12:
    print(b // 2)
else:
    print(0)
