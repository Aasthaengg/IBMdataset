from sys import stdin, exit

input = stdin.readline
lmi = lambda: list(map(int, input().split()))
mi = lambda: map(int, input().split())
si = lambda: input().strip('\n')
ssi = lambda: input().strip('\n').split()

a, b = mi()
if b / a % 1 == 0:
    print(a+b)
else:
    print(b-a)