a={1,3,5,7,8,10,12}
b={4,6,9,11}
c={2}

nums=[None]*12
for i in a:
  nums[i-1]="a"
for i in b:
  nums[i-1]="b"
for i in c:
  nums[i-1]="c"
x,y=map(int,input().split())
if nums[x-1]==nums[y-1]:
  print("Yes")
else:
  print("No")