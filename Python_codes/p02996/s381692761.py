import sys
N = int(input())
BA = [None] * N
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    BA[i] = (b, a)
BA.sort()

t = 0
for b, a in BA:
    t += a
    if b < t:
        print("No")
        break
else:
    print("Yes")