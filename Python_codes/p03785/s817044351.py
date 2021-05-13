import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n ,c, k = inintm()

T = []
ans = 1

for _ in range(n):
    T.append(inint())

T.sort()

f = T[0]
cnt = 1

for i in range(1,n):
    cnt += 1
    if T[i] - f <= k and cnt <= c:
        continue
    else:
        f = T[i]
        ans += 1
        cnt = 1

print(ans)