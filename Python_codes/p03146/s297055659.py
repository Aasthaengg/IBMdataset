s = int(input())
ans_list = [0] * (10 ** 6 + 1)
ans_list[0] = s
now = s

i = 1
T = True
while T:
  if now % 2 == 0:
    now = int(now / 2)
  else:
    now = 3 * now + 1
  i += 1
  if now in ans_list:
    print(i)
    T = False
  ans_list[i - 1] = now
  #print(now)
  #print(ans_list)
  
