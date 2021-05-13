N = int(input())
List = list(map(str, input().split()))
s_l = set(List)
if len(s_l) == 3:
  print("Three")
else:
  print("Four")