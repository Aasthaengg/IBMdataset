n = list(input())
ans = ''
for i in n:
  if int(i) == 1:
    i = '9'
  elif int(i) == 9:
    i = '1'
  ans += i
print(int(ans))