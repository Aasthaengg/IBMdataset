n = int(input())

strs = {}

for i in range(n):
    s = input().split()
    if(s[0] == 'insert'):
        if(s[1] not in strs):
            strs[s[1]] = ''
    else:
        if(s[1] in strs):
            print('yes')
        else:
            print('no')
