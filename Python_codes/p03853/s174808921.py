h,w = map(int,input().split())
c = []

while True:
  try:
    c.append(list(input().split()))    
  except:
    break
    
for i in c:
  for j in i:
    print(j)
    print(j,end="")
  print("")