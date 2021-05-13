#!/usr/bin/env python3

S = input()
K = int(input())

if len(S) == 1:
    print(K//2)
    exit()

cnt = 1
C = []
for i in range(1,len(S)):
    if S[i-1] == S[i]:
        cnt += 1
    else:
        C.append([S[i-1], cnt])
        cnt = 1
C.append([S[i], cnt])

ans = 0
if len(C) == 1:
    print((C[0][1]*K) // 2)
    exit()
else:
    for c in C:
        ans += c[1] // 2

ans *= K

ans2 = 0
if S[-1] == S[0]:
    ans2 = ((C[0][1]+C[-1][1])//2 - C[0][1]//2 - C[-1][1]//2) * (K-1)
print(ans + ans2)
