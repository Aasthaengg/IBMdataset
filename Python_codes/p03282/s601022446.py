s = input()
k = int(input())

n = len(s)
if n == 1 or k == 1: print(s[0])
else:
  for i in range(n):
    if s[i] == "1":
      k -= 1
      if k == 0: 
        print(s[i])
        break
    else:
      print(s[i])
      break