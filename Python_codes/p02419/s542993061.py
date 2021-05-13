w = input().lower()
t = ''
while(True):
    row = input()
    if row == 'END_OF_TEXT':
        break
    t += row.lower() + '\n'

print(t.split().count(w))