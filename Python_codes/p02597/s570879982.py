# coding: utf-8
N = int(input())
C = list(input())

R_cnt = 0

for i in range(N):
    if C[i] == "R":
        R_cnt += 1

ans = 0

for i in range(R_cnt):
    if C[i] == "W":
        ans += 1

print(ans)

