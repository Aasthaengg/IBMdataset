import sys
input = sys.stdin.readline

D,N=map(int,input().split())
if D == 0:
    if N < 100:
        ans = N
    else:
        ans = 101
elif D == 1:
    if N < 100:
        ans = N*100
    else:
        ans = 10100
else:
    if N < 100:
        ans = N * 10000
    else:
        ans = 1010000
print(ans)
