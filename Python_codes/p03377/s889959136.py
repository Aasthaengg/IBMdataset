cats, animal, num = map(int,input().split())
if num > cats + animal:
  print("NO")
elif cats > num:
  print("NO")
else:
  print("YES")