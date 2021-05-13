import sys
N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
t = sum(S)
if t % 10 != 0:
    print(t)
    sys.exit()

for s in S:
    if (t - s) % 10 != 0:
        print(t - s)
        sys.exit()
print(0)
