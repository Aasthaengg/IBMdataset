num_list = list(map(int, input().split(' ')))
N = num_list[0]
Y = num_list[1]
total = 0
ans = '-1 -1 -1'
for n in range(N+1):
  rest = N - n
  a = n*10000
  if rest == 0:
    if a == Y:
      ans = str(int(a/10000)) + ' 0 0'
      break
  for i in range(rest+1):
    rest_2 = rest - i
    b = i*5000
    c = rest_2*1000
    if rest == 0:
      if a+b == Y:
        ans = str(int(a/10000)) + ' ' + str(int(b/5000)) + ' 0'
        break
    elif a+b+c == Y:
      ans = str(int(a/10000)) + ' ' + str(int(b/5000)) + ' ' + str(int(c/1000))
print(ans)