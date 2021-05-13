import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = []
for _ in range(m):
    bc.append(list(map(int, input().split())))
bc = sorted(bc, reverse=True, key=lambda x: x[1])
cnt = n
for b, c in bc:
    if cnt <= b:
        for i in range(cnt):
            a.append(c)
        break
    else:
        for i in range(b):
            a.append(c)
        cnt -= b
a = sorted(a, reverse=True)
print(sum(a[:n]))

