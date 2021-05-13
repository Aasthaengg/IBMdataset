def calc_lucas(n):
  """
  Args:
    n (int)
  Returns:
    Luca_n (int)
  """
  luca = [0] * max((n + 1), 2)    # luca[i] = Luca_i
  luca[0] = 2
  luca[1] = 1
  for i in range(2, n+1):
    luca[i] = luca[i-1] + luca[i-2]
  return luca[n]
  



n = int(input())
print(calc_lucas(n))
