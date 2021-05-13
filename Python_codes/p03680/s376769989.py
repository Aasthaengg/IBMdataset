n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))
a = 1
for i in range(n):
  a = lst[a - 1]
  if a == 2:
    print(i + 1)
    exit()
print(-1)