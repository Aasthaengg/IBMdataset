import sys

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))  # applies to only numbers
rs = lambda: stdin.readline().rstrip()  # ignores trailing space

N = ri()
B = rl()
l = []
for i in range(N):
    if i + 1 < B[i]:
        print(-1)
        exit()

while B:
    for i in range(len(B)-1, -1, -1):
        if i + 1 == B[i]:
            l.append(B.pop(i))
            break

l = l[::-1]
print(*l, sep='\n')
# 47
