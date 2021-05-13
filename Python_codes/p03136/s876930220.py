n = input()
ls = list(map(int, input().split(" ")))

m = max(ls)
s = sum(ls)

if(s-m > m):
  print("Yes")
else:
  print("No")