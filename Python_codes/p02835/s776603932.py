a, b ,c = map(int, input().split())

if a + b + c <= 21:
  print("win")
  
elif a + b + c >= 21:
  print("bust")