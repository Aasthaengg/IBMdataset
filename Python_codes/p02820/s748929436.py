n,k = [int(i) for i in input().split()]
r,s,p = [int(i) for i in input().split()]
t = [i for i in input().split()[0]]
ts = [t[0+i::k] for i in range(k)]
for t in ts:
  for i in range(len(t)-1):
    if t[i] == t[i + 1]:
      t[i + 1] = 'n'
  for i in range(len(t)):
    if t[i] == 'r':
      t[i] = p
    if t[i] == 's':
      t[i] = r
    if t[i] == 'p':
      t[i] = s
    if t[i] == 'n':
      t[i] = 0
sc = [sum(t) for t in ts]
print(sum(sc))