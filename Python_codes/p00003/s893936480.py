N = int(raw_input())

for n in range(N):
  data_set = map(int, raw_input().split())
  a = data_set[0]
  b = data_set[1]
  c = data_set[2]

  if (a ** 2 + b ** 2) == (c ** 2) or (a ** 2 + c ** 2) == (b ** 2) or (b ** 2 + c ** 2) == (a ** 2):
    print "YES"
  else:
    print "NO"