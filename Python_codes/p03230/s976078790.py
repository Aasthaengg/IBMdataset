N, = map(int, raw_input().split())
r = "No"
for l in range(1,1000):
  if 2*N==l*(l+1):
    r = "Yes"
    break
print r
if r=="Yes":
  k = l+1
  S = []
  for i in range(k):
    S.append([])
  x = 1
  for i in range(k-1):
    for j in range(l-i):
      S[i].append(x)
      S[i+1+j].append(x)
      x += 1
  print k
  for i in range(k):
    print " ".join([str(l)] + map(str, S[i]))