n = int(input())
ls = [int(num) for num in input().split()]

ls.sort(reverse=True)

if (ls[0] < sum(ls[1:n])):
  print("Yes")
else:
  print("No")