import math
def main():
  N = int(input())
  s = 0
  if N % 2 == 0:
    s = 2 + N // 2

  for i in range(3, math.ceil(math.sqrt(N)) + 3):
    if N % i == 0 and (not s or s > i + N // i):
      s = i + N // i

  if not s:
    s = N + 1

  print(s-2)
  
main()