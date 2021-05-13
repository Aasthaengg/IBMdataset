num, sel = map(int, input().split(" "))
a = sorted(list((int)(input()) for i in range(num)))
mini = 10 ** 9
for i in range(num - sel + 1):
  if mini > a[i + sel - 1] - a[i]:
    mini = a[i + sel - 1] - a[i]
print(mini)