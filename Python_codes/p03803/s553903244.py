a, b = map(int, input().split())
if(a == 1):
  a = 14
if(b == 1):
  b = 14
[print("Alice") if a > b else print("Draw") if a == b else print("Bob")]