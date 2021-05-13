n = int(input())
a = list(map(int, input().split()))
negative = []
positive = []
cnt=0
for i in range(n):
  if a[i] < 0:
    cnt += 1
    negative.append(a[i])
  else:
    positive.append(a[i])
if cnt % 2 == 0:
  print(sum(map(lambda x: abs(x), a)))
elif cnt == len(a):
  a.sort()
  b = a[-1]
  a.remove(a[-1])
  print(b+sum(map(lambda x: abs(x), a)))
else:
  negative.sort()
  positive.sort()
  if abs(negative[-1]) < positive[0]:
    a.remove(negative[-1])
    print(negative[-1]+sum(map(lambda x: abs(x), a)))
  else:
    a.remove(positive[0])
    print(-positive[0]+sum(map(lambda x: abs(x), a)))