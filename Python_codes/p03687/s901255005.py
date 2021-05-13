def find_idx(s, c):
  idx_lst = [len(i) for i in s.split(c)]
  return idx_lst

s = input()
res = float('inf')
for i in range(97, 97 + 26):
  tmp = find_idx(s, chr(i))
  if tmp:
    res = min(res, max(tmp))
print(res)
