A,B = map(int, input().split())
arr = []
for i in range(B - A + 1, A + B):
  arr.append(i)
for i in arr:
  print(i,end=" ")