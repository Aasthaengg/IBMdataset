x,y=map(int, input().split())
group_a=[1,3,5,7,8,10,12]
group_b=[4,6,9,11]
group_c=[2]

if x in group_a and y in group_a:
  print("Yes")
elif x in group_b and y in group_b:
  print("Yes")
elif x in group_c and y in group_c:
  print("Yes")
else:
  print("No")