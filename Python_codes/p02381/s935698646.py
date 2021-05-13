while True:
  n = int(input())
  if n == 0: break
  A = list(map(int, input().split()))
  m = sum(A)/n
  N = (sum((a-m)**2 for a in A)/n)**0.5
  print(f"{N:.8f}")
