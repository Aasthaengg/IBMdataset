s = input()
remain=15-len(s)

maru=0
for i in s:
    if i =='o':
        maru+=1
        
if remain >= 8-maru:
    print('YES')
else:
    print('NO')
