nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()

R = n()

if R < 1200:
    print('ABC')
elif R < 2800:
    print('ARC')
else:
    print('AGC')
