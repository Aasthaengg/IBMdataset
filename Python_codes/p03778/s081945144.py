w,a,b = map(int,input().split())

if b < a-w:
  print(a-(b+w))
elif a-w<= b <= a+w :
  print("0")
elif a+w < b:
  print(b - (a+w))
