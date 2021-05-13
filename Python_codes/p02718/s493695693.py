n, m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
lst.reverse()
x = sum(lst)
if (lst[m - 1] < x/4/m):
  print("No")
else:
  print("Yes")
