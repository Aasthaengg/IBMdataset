n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
  print (-1)
  exit()
cnt = 0
d = [0] * n
s = 0
for i in range(n):
  d[i] = a[i]-b[i]
  if d[i] < 0:
    cnt += 1
    s += abs(d[i])
if cnt == 0:
  print (0)
  exit()

d.sort(reverse=True)

t = 0
for i in range(n):
  if s > d[i]:
    cnt += 1
    s -= d[i]
  else:
    cnt += 1
    break
print (cnt)