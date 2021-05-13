s = input()
for _ in range(int(input())):
  q = input()
  if q.startswith('replace'):
    q, a, b, p = q.split()
    a = int(a)
    b = int(b)
    s = s[:a]+p+s[b+1:]
  elif q.startswith('reverse'):
    q, a, b = q.split()
    a = int(a)
    b = int(b)
    s = s[:a]+s[a:b+1][::-1]+s[b+1:]
  elif q.startswith('print'):
    q, a, b = q.split()
    a = int(a)
    b = int(b)
    print(s[a:b+1])