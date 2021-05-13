X = int(input())
yen = 100
count = 0

while True:
  if yen >= X:
    break
  yen += yen // 100
  count += 1
  
print(count)

