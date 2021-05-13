s = input()

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
a = day.index(s)
ans = 7 - a
if ans == 0:
    print(7)
else:
    print(ans)