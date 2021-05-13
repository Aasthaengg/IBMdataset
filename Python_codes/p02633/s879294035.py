X=int(input())

count=1

while True:
  if X*count%360==0:
    break
  else:
    count=count+1

print(count)