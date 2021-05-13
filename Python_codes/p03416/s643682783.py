[A, B] = list(map(int, input().split()))
cnt = 0
for i in range(A, B+1):
  list_str = list(str(i))
  list_str_re = list(reversed(list_str))
  if list_str == list_str_re:
    cnt += 1
  else:
    continue
print(cnt)