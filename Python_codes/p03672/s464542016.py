s = list(input())

while True:
  s.pop()
  s.pop()
  t = len(s)//2
  if s[:t]==s[t:]:
    print(len(s))
    exit()