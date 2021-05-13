n = int(input())
a = sorted(list(map(int,input().split())))

if sum(a[:-1])>a[-1]:
  print("Yes")
else:
  print("No")
