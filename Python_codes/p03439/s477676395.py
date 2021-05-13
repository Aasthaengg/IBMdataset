n=int(input())
print(0, flush=True)
sl=input()
if sl=="Vacant":
  exit(0)

l=0
r=n-1

for i in range(30):

  if r-l<=2:
    for j in range(3):
      print(l+j+1, flush=True)
      s=input()
      if s=="Vacant":
        exit(0)

      
  elif ((l+r)//2)%2==0:
    print((l+r)//2, flush=True)
    s=input()
    if s=="Vacant":
      exit(0)
    elif s==sl:
      l=(l+r)//2
      sl=s
    else:
      r=(l+r)//2
      sr=s

  else:
    print((l+r)//2+1, flush=True)
    s=input()
    if s=="Vacant":
      exit(0)
    elif s==sl:
      l=(l+r)//2
      sl=s
    else:
      r=(l+r)//2
      sr=s