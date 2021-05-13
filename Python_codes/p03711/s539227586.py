a,b = list(map(int,input().split()))
c = [1,3,5,7,8,10,12]
d = [4,6,9,11]
e = [2]
if a in c and b in c:
  print("Yes")
elif a in d and b in d:
  print("Yes")
elif a in e and b in e:
  print("Yes")
else:
  print("No")