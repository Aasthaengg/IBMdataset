s = input()

j1 = s[0] == 'A'
j2 = s[2:-1].count('C') == 1
j3 = True

s3 = set(s) - set('AC')
for i in s3:
    if i != i.lower():
        j3 = False
        break

print('AC') if j1 and j2 and j3 else print('WA')