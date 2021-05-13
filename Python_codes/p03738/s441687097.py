from sys import stdin
from numpy import argmin

a = int(stdin.readline().strip())
b = int(stdin.readline().strip())

if a > b:
  print('GREATER')
elif a < b:
  print('LESS')
else:
  print('EQUAL')