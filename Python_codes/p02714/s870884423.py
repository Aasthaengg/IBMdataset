# -*- conding: utf-8 -*-
import math
N = int(input())
S = input()

count_R = 0
count_G = 0
count_B = 0
for s in S:
  if s == "R":
    count_R += 1
  elif s == "G":
    count_G += 1
  else:
    count_B += 1

count = 0
for i in range(N-2):
  for j in range(i+1, (N+1+i)//2):
    if S[i] != S[j] and S[i] != S[j+(j-i)] and S[j] != S[j+(j-i)]:
      count += 1

print(count_R * count_G * count_B - count)