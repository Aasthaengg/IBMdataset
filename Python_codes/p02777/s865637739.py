s, t = (x for x in raw_input().split())
a, b = (int(x) for x in raw_input().split())
u = raw_input()
if s == u:
  a -= 1
else:
  b -= 1
print "{} {}".format(a, b)