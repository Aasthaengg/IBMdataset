N = int(input())
S = list(input())
x=0
maxa=0
for s in S:
  if s=="I":
    x+=1
  else:
    x-=1
  maxa=max(x, maxa)
print(maxa)