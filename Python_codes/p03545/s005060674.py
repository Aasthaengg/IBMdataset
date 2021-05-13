s = list(input())
ans = []
for i in ['+', '-']:
    for j in ['+', '-']:
        for k in ['+', '-']:
            tmp = int(s[0])
            if i == '+':
                tmp += int(s[1])
            else:
                tmp -= int(s[1])
            if j == '+':
                tmp += int(s[2])
            else:
                tmp -= int(s[2])
            if k == '+':
                tmp += int(s[3])
            else:
                tmp -= int(s[3])
            if tmp == 7:
                ans = [s[0],i,s[1],j,s[2],k,s[3],'=7']
                break
print(''.join(map(str,ans)))