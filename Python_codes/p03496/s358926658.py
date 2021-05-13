n = int(input())
a = list(map(int, input().split()))
count = 0
outs = []
max_a = max(a)
max_index = a.index(max(a))
min_a = min(a)
min_index = a.index(min(a))
flag = -1
if 0 <= min_a:
  flag = 0
elif max_a <= 0:
  flag = n
elif max_a > -1 * min_a:
  flag = 0
  for i in range(0,n):
    if a[i] < 0:
      a[i] += max_a
      outs.append(str(max_index + 1) + " " + str(i + 1))
      count += 1
elif max_a <= -1 * min_a:
  flag = n
  for i in range(0,n):
    if a[i] > 0:
      a[i] += min_a
      outs.append(str(min_index + 1) + " " + str(i + 1))
      count += 1

if flag == 0:
  for i in range(0, n-1):
    a[i+1] += a[i]
    outs.append(str(i + 1) + " " + str(i + 1 + 1))
    count += 1
elif flag == n:
  for i in range(1, n):
    a[n-i-1] += a[n-i]
    outs.append(str(n - i + 1) + " " + str(n - i - 1 + 1))
    count += 1
    
print(count)
for out in outs:
  print(out)