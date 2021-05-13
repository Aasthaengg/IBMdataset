#!/usr/bin/env python3

R, G, B, N = map(int, input().split())

ans = 0
cnt = 0
cnt2 = 0
for i in range(N+1):
    cnt = R * i
    for j in range(N+1):
        cnt2 = cnt + G * j
        if cnt2 == N:
            ans += 1
            continue
        if cnt2 > N:
            continue
        else:
            nokori = N - cnt2
            if nokori % B == 0:
                ans += 1
print(ans)
