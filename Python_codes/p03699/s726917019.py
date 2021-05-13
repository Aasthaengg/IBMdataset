import sys
N = int(input())
s = [int(input()) for _ in range(N)]
S = sum(s)
if S % 10 != 0:
    print(S)
    sys.exit()
M = 0
for si in s:
    T = S - si
    if T % 10 != 0:
        M = max(M, T)
print(M)