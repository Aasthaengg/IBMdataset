while 1:
 n = input()
 if int(n) == 0:
  break
 sum = 0
 for i in range(len(n)):
  sum += int(n[i])
 print(sum)