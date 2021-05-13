import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

k = ni()
n = 50

a = k//n
b = k%n
c = n-1+a

ans = [str(c+n-b+1)]*b + [str(c-b)]*(n-b)

print(n)
print(' '.join(ans))
