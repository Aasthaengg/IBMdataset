S = input()
youbi =['MON','TUE','WED','THU','FRI','SAT','SUN']
nissu = 6-youbi.index(S)
if nissu == 0:
    nissu = 7
print(nissu)