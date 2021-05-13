#!/usr/bin/env python3

N = int(input())
A = [0]
for i in range(N):
    A.append(int(input()))

i = 1
ans = 0
flg = False
while A[i] != 0 and not flg:
    if i == 2:
        flg = True
    else:
        ans += 1
        tmp = i
        i = A[i]
        A[tmp] = 0

if flg:
    print(ans)
else:
    print(-1)


