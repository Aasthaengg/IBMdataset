a,b = map(int,input().split())
num = a * b
mod = num % 2

if mod == 0:
  print("Even")
else:
  print("Odd")