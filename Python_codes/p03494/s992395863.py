n = int(input())
a = map(int, input().split())

ans = 0
isEven = True

while isEven:
  list_tmp = []
  for an in a:
    if an % 2 ==0:
      list_tmp.append(an / 2)
    else:
      isEven = False
      break;
  a = list_tmp
  ans += 1

print(ans - 1)
