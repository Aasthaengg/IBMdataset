# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

for i in range(1, N):
  if A[i-1] == A[i]:
    print("NO")
    exit()
print("YES")