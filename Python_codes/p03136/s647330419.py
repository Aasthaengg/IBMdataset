n = int(input())
a = list(map(int,input().split()))
a_max = max(a)
a.remove(a_max)
if a_max < sum(a):
  print("Yes")
  
else:
  print("No")