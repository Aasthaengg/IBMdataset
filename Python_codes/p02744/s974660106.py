N = int(input())

def main(l):
  tmp = []
  for a in l:
    n = a[1]
    for i in range(97, n+2):
      tmp.append([a[0]+chr(i), max(i, n)])
  return tmp
  
l = [['a', 97]]
for i in range(1, N):
  l = main(l)
for i in range(len(l)):
  print(l[i][0])