s = input()

for i in range(1,len(s)+1,2):
    if s[i-1] == 'L':
        print('No')
        break
else:
    for i in range(2,len(s)+1,2):
        if s[i-1] == 'R':
            print('No')
            break
    else:
        print('Yes')