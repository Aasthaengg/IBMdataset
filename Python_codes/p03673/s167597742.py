def make_indices_list(n):
  """
  Args:
    n (int)

  >>> make_indices_list(8):
  [7, 5, 3, 1, 0, 2, 4, 6]
  >>> make_indices_list(7):
  [6, 4, 2, 0, 1, 3, 5]
  """
  if n % 2 == 0:
    return list(range(n-1, 0, -2)) + list(range(0, n, 2))
  else:
    return list(range(n-1, -1, -2)) + list(range(1, n-1, 2))
    


n = int(input())
L = list(map(int, input().split()))

indices_list = make_indices_list(n)
for ind in indices_list:
  print(L[ind], end=' ')
print('')
