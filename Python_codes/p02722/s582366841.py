N=int(input())

def cf(n):
  a=[]
  f=1
  while f*f<=n:
    if n%f==0:
      a.append(f)
      if n//f!=f:
        a.append(n//f)
    f+=1
  return a

def main():
  c=len(cf(N-1))-1
  for f in cf(N):
    t=N
    if f!=1:
      while t%f==0:
        t//=f
      if t%f==1:
        c+=1
  print(c)

main()
