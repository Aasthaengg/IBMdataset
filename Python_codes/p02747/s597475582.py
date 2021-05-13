s = input()
oza = 'hi'
flag = 0
for i in range(0,len(s),2):
    if s[i:i+2] == oza:
        continue
    else:
        flag = 1
        print('No')
        break
if flag == 0:
    print('Yes')
