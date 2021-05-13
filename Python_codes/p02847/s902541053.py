S = str(input())
week = ['SAT','FRI','THU','WED','TUE','MON','SUN']

for i in range(7):
  if S == week[i]:
    print(i+1)