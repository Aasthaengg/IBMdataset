def find_max_rectangle(pair):
  """
  Args:
    pair (list): reversely sorted 
  Returns:
    area (int)
  """
  if len(pair) >= 2:
    M = pair[0]
    second_max = pair[1]
    return M * second_max
  else:
    return 0



n = int(input())
L = list(map(int, input().split()))
L.sort()
pair = []
prev = None
while L:
  popped = L.pop()
  if prev == popped:
    pair.append(prev)
    prev = None
  else:
    prev = popped

print(find_max_rectangle(pair)) 
