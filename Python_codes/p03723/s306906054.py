a, b, c = map(int, input().split())

count = 0

while True:  
  if a%2 == b%2 == c%2 == 0:
    if a == b == c:
      print(-1)
      exit()
    a, b, c = (b+c)/2, (a+c)/2, (a+b)/2
    count += 1
  else:
    break

print(count)