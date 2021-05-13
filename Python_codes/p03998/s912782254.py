sa = input()
sb = input()
sc = input()

t = "a"
while True:
  if t == "a":
    if len(sa) == 0: break
    t = sa[0]
    sa = sa[1:]
  elif t == "b":
    if len(sb) == 0: break
    t = sb[0]
    sb = sb[1:]
  elif t == "c":
    if len(sc) == 0: break
    t = sc[0]
    sc = sc[1:]

print(t.upper())