while True:
 al=input()
 if al=='-':
     break
 else:
  m=int(input())
  for i in range(m):
   n = int(input())
   al= al[n:] + al[:n]
  print(al)