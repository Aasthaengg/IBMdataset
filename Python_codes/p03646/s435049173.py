k=int(input())
if k==0:
  print(2)
  print(0,0)
elif k==1:
  print("""3
1 0 3
""")
elif k<=50:
  print(k)
  print(*[k for i in range(k)])
else:
  print(50)
  rep=k//50
  rem=k%50
  l=[]
  for i in range(50):
    if i<rem:
      l.append(50+rep-rem+50)
    else:
      l.append(50+rep-1-rem)
  print(*l)