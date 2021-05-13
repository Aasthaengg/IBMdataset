N = int(input())
a = list(map(int,input().split()))
a = sorted(a)
b = a.pop()
if sum(a) > b:
  print("Yes")
else:
  print("No")