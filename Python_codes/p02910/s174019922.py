s = str(input())

for i in range(len(s)):
    #print(s[i])
    if i%2 == 0:        #偶数
        if s[i] != 'R' and s[i] != 'U' and s[i] != 'D':
            print('No')
            exit()
    elif i%2 == 1:       #奇数
        if s[i] != 'L' and s[i] != 'U' and s[i] != 'D':
            print('No')
            exit()
    

print('Yes')