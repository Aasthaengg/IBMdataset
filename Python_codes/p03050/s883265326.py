import sys

N = int(sys.stdin.readline())

ans = 0
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        j = N // i - 1
        if i < j:
            ans += j
    
print(ans)