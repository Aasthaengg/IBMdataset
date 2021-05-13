s = input()
r = 100;
for x in range(97, 97+26):
  cnt = 0
  m = 0
  for c in s:
    if c == chr(x):
      m = max(m, cnt)
      cnt = 0
    else:
      cnt += 1
  m = max(m, cnt)
  r = min(r, m)
print(r)