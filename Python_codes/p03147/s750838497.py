#!/usr/bin/env python3

N = int(input())
H = list(map(int, input().split()))
ret = 0

for c in range(100):
    f = False
    cnt = 0
    if H.count(0) == N: break
    for i in range(N):
        if H[i] > 0:
            H[i] -= 1
            f = True
        else:
            if f == True:
                cnt += 1
                f = False

        if i == N-1 and f == True:
            cnt += 1

    ret += cnt

print(ret)
