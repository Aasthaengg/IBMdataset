n = int(input())
a = [int(input()) for l in range(n)]
count = 0
for i in range(n):
  if a[count] == 2:
    print(i+1)
    exit()
  else:
    count = a[count]-1
print(-1)