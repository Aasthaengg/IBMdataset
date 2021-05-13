s=input()[::-1]
i=0
while i<len(s):
    if i+5<=len(s) and s[i:i+5]=='esare':
        i+=5
    elif i+5<=len(s) and s[i:i+5]=='maerd':
        i+=5
    elif i+6<=len(s) and s[i:i+6]=='resare':
        i+=6
    elif i+7<=len(s) and s[i:i+7]=='remaerd':
        i+=7
    elif i<len(s):
        print('NO')
        exit()
print('YES')