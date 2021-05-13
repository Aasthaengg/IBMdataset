n = int(input())
a = list(map(int,input().split()))
a = sorted(a)

if a[-1]<sum(a[0:n-1]):
  print("Yes")
else:
  print("No")