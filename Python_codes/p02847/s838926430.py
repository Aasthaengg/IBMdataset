S = input()
week =['SUN','MON','TUE','WED','THU','FRI','SAT']
for i in week:
    if i == S:
        a=week.index(i)
        print(7-a)
        exit()