n = int(input())
l = list(map(int,input().split()))
l1 = set(l)
if (len(l)-len(l1))%2==0:
  print(len(l1))
else:
  print(len(l1)-1)