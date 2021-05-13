import itertools
n = int(input())
a_li = []
x_li = []
y_li = []
for i in range(n):
  a = int(input())
  a_li.append(a)
  tmp_x = []
  tmp_y = []
  for j in range(a):
    x, y = list(map(int, input().split()))
    x -= 1
    tmp_x.append(x)
    tmp_y.append(y)
  x_li.append(tmp_x)
  y_li.append(tmp_y)
total_li = list(itertools.product([0, 1], repeat=n))
ans = 0
for each in total_li:
  flag = True
  for i, person in enumerate(each):
    if person == 1:
      per_li = x_li[i]
      hone_li = y_li[i]
      for pe, ho in zip(per_li, hone_li):
        if each[pe] != ho:
          flag = False

  if flag:
    ans = max(ans, sum(each))
print(ans)