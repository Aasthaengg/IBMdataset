import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
a = [I() for _ in range(N)]

b = sum(a[i] % 2 for i in range(N))
print('second' if b == 0 else 'first')
