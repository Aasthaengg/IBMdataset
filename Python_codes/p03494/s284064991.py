n = int(input())
a = map(int, input().split())

ans = 0
isEven = True

while isEven:
  list_tmp = []
  for an in a:
    q, mod = divmod(an, 2)
    if mod ==0:
      list_tmp.append(q)
    else:
      isEven = False
      break;
  a = list_tmp
  ans += 1

print(ans - 1)
