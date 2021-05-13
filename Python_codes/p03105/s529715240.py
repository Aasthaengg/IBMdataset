a,b,c = map(int,input().split())
count = int(b / a)

if count >= c:
  print(c)
else:
  print(count)