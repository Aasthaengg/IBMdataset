a={1,3,5,7,8,10,12}
b={4,6,9,11}
c={2}
xy=set(map(int,input().split()))
if xy.issubset(a) or xy.issubset(b) or xy.issubset(c):
  print("Yes")
else:
  print("No")
