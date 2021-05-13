s=input()
y=int(s[0:4])
m=int(s[5:7])
if y<2019:
  print('Heisei')
elif y==2019 and m<5:
  print('Heisei')
else:
  print('TBD')