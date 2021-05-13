s = input()

if s.find('RRR') != -1:
  print(3)
elif s.find('RR') != -1:
  print(2)
elif s.find('R') != -1:
  print(1)
else:
  print(0)