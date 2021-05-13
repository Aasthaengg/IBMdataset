import math
N = int(input())
h = list(map(int, input().split()))
ans = 0
while sum(h) > 0:
    i = 0
    while i < N and h[i] == 0:
        i += 1
    if i < N:
        ans += 1
        while i < N and h[i] > 0:
            h[i] -= 1
            i += 1
print(ans)
