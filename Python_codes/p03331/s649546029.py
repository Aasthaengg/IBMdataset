s = input()
l = len(s)
a = [int(x) for x in s]
 
if int(s) == 10 ** (l - 1):
  print(10)
else:
  print(sum(a))