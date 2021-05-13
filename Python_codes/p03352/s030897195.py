n = int(input())
a = []
tent = True
while True:
  if tent == True:
    for i in range(1,1001):
      if i ** 2 > 1000:
        tent = False
        break
      else:
        for j in range(2,10):
          if i**j <= 1000:
            a.append(i**j)
          else:
            break
  else:
    break
new_lst = [e for e in a if e <= n]
print(max(new_lst))