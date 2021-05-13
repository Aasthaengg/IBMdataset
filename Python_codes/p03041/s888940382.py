nk = input().split()
index = int(nk[1]) -1
s = input()
c = 0
for i in s:
  if c == index: print(i.lower(),end="")
  else: print(i,end="")
  c+= 1