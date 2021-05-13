from sys import stdin
from numpy import argmin

a,b = [int(x) for x in stdin.readline().split()]
cnt = 0

for i in range(a, b+1):
  si = str(i)
  if si == si[::-1]:
    cnt += 1
    
print(cnt)