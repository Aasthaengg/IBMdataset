import io
import math

data = int(input())
nim,mike = 1,1
for _ in range(data):
  n,m = [int(_) for _ in input().split(" ")]
  l = max(-(-nim//n), -(-mike//m))
  nim,mike = l*n,l*m
print(nim+mike)