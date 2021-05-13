S = input()

def pj(cond):
  print({True: "Yes", False:"No"}[cond])

d = {}
for c in S:
  if c in d:
    d[c] += 1
  else:
    d[c] = 1
if len(d.keys()) != 2:
  pj(False)
  exit(0)
if not all(i == 2 for i in d.values()):
  pj(False)
  exit(0)
pj(True)