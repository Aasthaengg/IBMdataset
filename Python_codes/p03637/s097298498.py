n=int(input())
a=list(map(int,input().split()))
count4=0
count2=0

for i in a:
  if i%4==0:
    count4+=1
  elif i%2==0:
    count2+=1

if count2<1:
  count1=len(a)-count4
else:
  count1=len(a)-count4-count2+1
if count1-count4<=1:
  print("Yes")
else:
  print("No")