S=input()
can=[]
sta=['AKIHABARA']
while sta:
    s=sta.pop()
    can.append(s)
    for i,x in enumerate(s):
        if x=='A':
            sta.append(s[:i]+s[i+1:])
print('YES' if S in set(can) else 'NO')