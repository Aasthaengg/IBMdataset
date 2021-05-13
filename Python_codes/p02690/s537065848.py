x = int(input())

flag = False
for i in range(1000, -1, -1):
  #print(i)
  for j in range(i, -1001, -1):
    #print(j)
    if i - j != 0:
      if x % (i - j) == 0:
        y = x / (i - j)
        t = i ** 4 + (i ** 3) * j + (i ** 2) * (j ** 2) + i * (j ** 3) + j ** 4
        if y == t:
          lst = [str(i), str(j)]
          print(' '.join(lst))
          flag = True
          break
    else:
      if x == 0:
        print('0 0')
        flag = True
        break
  if flag:
    break
