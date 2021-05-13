N, x = input().split(' ')
N = int(N)
x = int(x)
a = input().split(' ')
a = [int(a[i]) for i in range(N)]
a = sorted(a)
count = 0
for i in range(N):
  if x - a[i] < 0:
    x -= a[i]
    break
  else:
    x -= a[i]
    count += 1
if x > 0:
  count -= 1

print(count)