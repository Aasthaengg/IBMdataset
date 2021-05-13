s = input()
count = 0
s = s.replace('BC','X')
s = s.replace('B','Z').replace('C','Z')
s = s.split('Z')
for i in s:
    ac = 0
    for j in range(len(i)):
        if i[j] == 'A':
            ac += 1
        if i[j] == 'X':
            count += ac
print(count)