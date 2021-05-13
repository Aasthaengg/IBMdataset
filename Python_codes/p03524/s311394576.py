s=list(input())
a=0
b=0
c=0
for i in range(len(s)):
    if s[i]=='a':
        a+=1
    elif s[i]=='b':
        b+=1
    else:
        c+=1
if(a<(int(len(s)/3)) or b<(int(len(s)/3)) or c<(int(len(s)/3))):
    print('NO')
else:
    if len(s)%3!=2:
        print('YES')
    else:
        if max(a,b,c)==(int(len(s)/3)+2):
            print('NO')
        else:
            print('YES')
