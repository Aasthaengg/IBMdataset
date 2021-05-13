x = int(input())
a = int(input())
b = int(input())
yen = x -a 
while True:
  yen -= b
  if yen < 0:
    yen += b
    break
print(yen)
