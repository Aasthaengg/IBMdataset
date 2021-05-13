N = input()

while 1:
  l = []
  for i in range(len(N)):
    l.append((int(N[i])))
  
  if min(l) == max(l):
    print(N)
    break
  else:
    N = str(int(N) + 1)