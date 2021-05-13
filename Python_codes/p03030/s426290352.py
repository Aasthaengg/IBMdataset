N = int(input())
lst = []
for i in range(N):
  s, p = input().split()
  lst.append([s, int(p), i+1])
lst = sorted(lst, key = lambda x: x[1], reverse=True)
lst = sorted(lst, key = lambda x: x[0])
for j in range(N):
  print(lst[j][2], end=" ")