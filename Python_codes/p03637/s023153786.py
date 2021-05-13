n = int(input())
l = list(map(int,input().split()))
c = len([i for i in l if i%4==0])
l1 = [i for i in l if  (i%2==0 and i%4!=0)]
if len(l1)>=1:
  a = n-len(l1)+1
  a = a-c
  if a<=c+1:
    print("Yes")
  else:
    print("No")
else:
  a = n-c
  if a<=c+1:
    print("Yes")
  else:
    print("No")