a,b = [int(a) for a in input().split()]
if b%2==0:
  if a>=13:
    print(b)
  elif 6<=a<=12:
    print(int(b/2))  
  elif a<=5:
    print(0)  