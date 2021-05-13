n=int(input())
def out(t):
  print(t,flush=True)
  s=input()
  if s=='Male':return 0
  elif s=='Female':return 1
  else:exit()
l=0
r=n
f=out(0)
while l+1!=r:
  m=(l+r)//2
  if (m+f)%2==out(m):l=m
  else:r=m