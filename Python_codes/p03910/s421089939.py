import sys
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
m = 10**7
a = 1
i = 1

while a <= m:
    if a >= n:
        break
    i+=1
    a+=i

ans = [j for j in range(1,i+1) if j != a-n]

print(*ans,sep="\n")