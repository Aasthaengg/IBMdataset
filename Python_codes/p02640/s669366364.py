x,y = map(int,input().split())

def check():
  for i in range(x+1):
    k = x - i
    n = i * 2 + k * 4
    if n == y:
      return True
  return False

if check():
  print("Yes")
else:
  print("No")