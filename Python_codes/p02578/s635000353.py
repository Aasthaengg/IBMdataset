from typing import List

def step(n: int, a: List[int])-> int:
  result = 0
  dai = 0
  for i in range(1,n):
    sub = a[i-1] + dai - a[i]
    if sub > 0:
      dai = sub      
      result += sub
      continue
    dai = 0
  return result

if __name__ == "__main__":
  n = int(input())
  a = list(map(int, input().split()))
  print(step(n, a))