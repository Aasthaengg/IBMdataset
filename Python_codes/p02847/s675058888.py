S = input()
days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
i = 0
for d in reversed(days):
    i += 1
    if d == S:
        break
print(i)
