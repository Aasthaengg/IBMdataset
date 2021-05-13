s = input()
youbi = ['SUN','MON','TUE','WED','THU','FRI','SAT']
index = youbi.index(s)

day = 7 - index
if day == 0:
  print('7')
else:
  print(day)