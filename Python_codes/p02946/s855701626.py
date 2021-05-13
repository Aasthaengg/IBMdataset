a,k = map(int, input().split())
arr = []
for i in range(k - a + 1, a + k):
  arr.append(i)
for i in arr:
  print(i,end=" ")
