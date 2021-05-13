n = int(input())
list_length = list(map(int, input().split()))
MAX = max(list_length)
list_length.remove(MAX)
if sum(list_length) > MAX:
  print("Yes")
else:
  print("No")