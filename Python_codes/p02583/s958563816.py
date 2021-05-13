# -*- coding: utf-8 -*-
N = int(input())
L = list(map(int, input().split()))
ans = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      a = L[i]
      b = L[j]
      c = L[k]
      if a + b > c and a + c > b and b + c > a and a != b and a != c and b != c:
        ans += 1
print(ans)