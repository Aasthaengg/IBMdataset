import math

def solve(ratio_list):
  a = 0
  b = 0
  for p, q in ratio_list:
    if a == 0 and b == 0:
      a = p
      b = q
    else:
      fact1 = -(-a//p)
      fact2 = -(-b//q)
      factor = int(max(fact1, fact2))
      a = factor*p
      b = factor*q
  return a,b


if __name__ == "__main__":
  n = int(input())
  ratio = [tuple(map(int, input().split())) for _ in range(n)]
  a,b = solve(ratio)
  print(a+b)
