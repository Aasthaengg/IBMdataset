# coding: utf-8
# Your code here!
import sys

n = int(input())
h = list(map(int, input().split()))
h = h[::-1]
for i in range(1, n):
  if h[i] >= h[i-1] + 2:
    print("No")
    sys.exit()
  elif h[i] == h[i-1] + 1:
    h[i] -= 1
print("Yes")    
