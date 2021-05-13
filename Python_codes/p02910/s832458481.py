s = input()
n = len(s)


for i in range(n):
    if (i+1)%2 == 0 and s[i] == 'R':
        print('No')
        break
    elif (i+1)%2 == 1 and s[i] == 'L':
        print('No')
        break
else:
    print('Yes')