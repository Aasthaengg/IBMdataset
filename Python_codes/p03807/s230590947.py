# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split()))

even = odd = 0
for i in range(N):
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if odd % 2 != 0:
    print("NO")
else:
    print("YES")
