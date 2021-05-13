s = input()
n = len(s)
ans = 'Yes'
for i in range(n):
    if i%2 == 0:
        if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
            ans = 'Yes'
        else:
            print('No')
            exit()

    else:
        if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
            ans = 'Yes'
        else:
            print('No')
            exit()

print(ans)