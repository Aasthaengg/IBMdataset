s = input()
min_change = 100
for char in 'abcdefghijklmnopqrstuvwxyz':
    absence = 0
    max_absence = 0
    for i in s:
        if i != char:
            absence += 1
        else:
            max_absence = max(max_absence,absence)
            absence = 0
    max_absence = max(max_absence,absence)
    min_change = min(min_change,max_absence)
print(min_change)