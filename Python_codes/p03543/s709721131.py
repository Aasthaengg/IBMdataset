def is_good_num(n):
  """
  Arg:
    n (str) 
  Returns:
    bool
  """
  return (n[0] == n[1] and n[1] == n[2]) or (n[1] == n[2] and n[2] == n[3])
  


n = input()
print('Yes') if is_good_num(n) else print('No')
