from math import floor
A,B,N = map(int,input().split())
def floor_1(x):
  return floor(A*x/B) - floor(x/B)*A
print(floor_1(min(N,B-1)))