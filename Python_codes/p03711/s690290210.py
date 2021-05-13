x,y=map(int,input().split())

set1={1,3,5,7,8,10,12}
set2={4,6,9,11}
set3={2}

if x in set1 and y in set1:
  print("Yes")
elif x in set2 and y in set2:
  print("Yes")
else:
  print("No")