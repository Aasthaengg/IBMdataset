input()
a = list(map(int, input().split()))
l = len(list(filter(lambda x : x & 1, a)))
if l & 1:
  print("NO")
else:
  print("YES")