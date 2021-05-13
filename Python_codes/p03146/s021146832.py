def f(x):
  if x%2==0:
    return x//2
  else:
    return 3*x+1

s = int(input())
old = s
count=1
history={s}
while 1:
  new = f(old)
  count += 1
  if new in history:
    break
  history.add(new)
  old = new

print(count)