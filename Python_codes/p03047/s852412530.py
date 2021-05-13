x,y = map(int,input().split())
count = 0
while count+y <= x:
  count += 1

print(count)