N=int(input())
a=[int(input()) for _ in range(N)]

visited={1,}
old=1
count=0
while 1:
  new = a[old-1]
  count += 1
  if new in visited:
    print(-1)
    exit()
  if new == 2:
    print(count)
    exit()
  old = new
  visited.add(new)