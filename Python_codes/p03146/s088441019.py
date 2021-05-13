#!/usr/bin/env python3

s = int(input())

A = [s]
for i in range(1,1000000+1):
    if A[i-1] % 2 == 0:
        a = A[i-1] // 2
    else:
        a = A[i-1]*3+1
    if a in A:
        ans = i+1
        break
    else:
        A.append(a)

print(ans)
