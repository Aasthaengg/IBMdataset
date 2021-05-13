s = input()
cnt = 0

if s[0] == 'A':
    for i in s[2:-1]:
        if i == 'C':
            cnt += 1
    if cnt == 1:
        s = s.replace('A', '')
        s = s.replace('C', '')
        if s.islower() and ('C' not in s):
            print('AC')
            exit()
print('WA')