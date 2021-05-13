N=int(input())
A=[int(a) for a in input().split()]

for a in A:
  if not a%2:
    if (a%3!=0 and a%5!=0):
      print('DENIED')
      break
else:
  print('APPROVED')
