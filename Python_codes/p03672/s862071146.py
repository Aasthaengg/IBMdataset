s = list(input())
s.pop(-1)
while len(s) > 0:
  if len(s) % 2 == 1:
    s.pop(-1)
    continue
  n = len(s)//2
  a = "".join(s[:n])
  b = "".join(s[n:])
  if a == b:
    print(len(s))
    exit()
  s.pop(-1)