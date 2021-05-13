n = int(input())
l = list(map(int,input().split()))
x = len(set(l))
if x%2 == 1:
  print(x)
else:
  print(x-1)