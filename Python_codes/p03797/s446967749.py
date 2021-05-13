s,c=map(int,input().split())
if s*2>=c:
  print(c//2)
else:
  print(s+(c-2*s)//4)