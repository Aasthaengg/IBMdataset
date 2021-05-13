from sys import stdin
from heapq import nsmallest

def second_smallest(numbers):
    return nsmallest(2, numbers)[-1]

a,b,c = [int(x) for x in stdin.readline().strip().split()]

if a%2==0 or b%2==0 or c%2==0:
  print(0)
else:
  print(min([a,b,c]) * second_smallest([a,b,c]))