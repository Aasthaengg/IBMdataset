from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)

input = stdin.readline
lmi = lambda: list(map(int, input().split()))
mi = lambda: map(int, input().split())
si = lambda: input().strip('\n')
ssi = lambda: input().strip('\n').split()
ii = lambda: int(input())

x, a = mi()
if x<a:
    print("0")
else:
    print("10")
