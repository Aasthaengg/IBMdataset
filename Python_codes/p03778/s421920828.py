W,a,b=map(int, input().split())

if a+W<=b:
  print(b-(a+W))
elif a+W>b and a<=b:
  print(0)
elif a>b and a<b+W:
  print(0)
elif a>=b+W:
  print(a-(b+W))