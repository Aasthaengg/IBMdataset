import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

h,w,a,b = na()
ans = []

for i in range(h):
    a = min(a,w-a)
    k = '0'*a + '1'*(w-a) if i < b else '1'*a+'0'*(w-a)
    ans.append(k)

print(*ans, sep='\n')