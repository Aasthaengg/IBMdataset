l = list(map(str, input().split()))

if l[0] == l[1]:
  print(l[2])
elif l[0] == l[2]:
  print(l[1])
elif l[1] == l[2]:
  print(l[0])