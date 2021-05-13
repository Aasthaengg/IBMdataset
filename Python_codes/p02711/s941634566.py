n = int(input())

if n//100 != 7 and (n-(n//100)*100)//10 != 7 and n-(n//10)*10 != 7:
  print('No')
else:
  print('Yes')