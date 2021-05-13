res = {
  ('H', 'H'): 'H',
  ('H', 'D'): 'D',
  ('D', 'H'): 'D',
  ('D', 'D'): 'H'
}
print(res[tuple(input().split())])
