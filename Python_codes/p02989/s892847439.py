n = int(input())
d = [int(num) for num in input().split()]

d.sort()
if d[len(d)//2] == d[len(d)//2 - 1]:
  print(0)
else :
  print(d[len(d)//2] - d[len(d)//2 - 1])