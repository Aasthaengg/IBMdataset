o = input()
e = input()

ans = []
n = 0
while n < len(o)+len(e):
  if n % 2 == 0:
    ans.append(o[n//2])
  else:
    ans.append(e[n//2])
  n += 1
print(*ans, sep='')