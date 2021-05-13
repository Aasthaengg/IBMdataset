import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
a = 1
while a <= N:
    if 2*a > N:
        print(a)
    a *= 2
