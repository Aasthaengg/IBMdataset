N = int(input())
next = []
for i in range(N):
  next.append(int(input()) - 1)
now = 0
count = 0
judge = False
for i in range(N):
  now = next[now]
  count += 1
  if now == 1: 
    judge = True
    print(count)
    break
if not judge:
  print(-1)