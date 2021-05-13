def find_idx(s, c):
  idx_lst = []
  while c in s:
    idx = s.index(c)
    idx_lst += [idx]
    s = s[idx+1:]
  else:
    idx_lst += [len(s)]
  return idx_lst

s = input()
res = float('inf')
for i in range(97, 97 + 26):
  tmp = find_idx(s, chr(i))
  if tmp:
    res = min(res, max(tmp))
print(res)
