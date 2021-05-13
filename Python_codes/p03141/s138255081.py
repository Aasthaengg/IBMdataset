import sys

readline = sys.stdin.readline
n = int(readline())
A = []
B = []
AB = []
for i in range(n):
    a, b = map(int, readline().split())
    A.append(a)
    B.append(b)
    AB.append(a+b)
AB.sort()
ans = -sum(B) + sum(AB[::-2])
print(ans)
