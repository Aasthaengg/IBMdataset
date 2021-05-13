input()
l=list(map(int,input().split()))
def f(b):
  c=s=0
  for i in l:
    if b:
      if s+i>0: s+=i
      else: c-=s+i-1; s=1
    else:
      if s+i<0: s+=i
      else: c+=s+i+1; s=-1
    b=1-b
  return c
print(min(f(0),f(1)))