weekday = input()

list = ['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in list:
    if weekday == i:
        daynum = list.index(weekday)

next = 7 - daynum

print(next)