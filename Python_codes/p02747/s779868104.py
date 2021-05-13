import sys

stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

s = ns()
for i in range(1,10):
    if s == 'hi'*i:
        print('Yes')
        break
else:
    print('No')
