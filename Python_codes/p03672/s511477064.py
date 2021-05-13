s = input()
n = len(s)
for i in range(n // 2):
  t = s[:n - 2 * (i + 1)]
  m = len(t) // 2
  if t[:m] == t[m:]:
    print(len(t))
    exit()