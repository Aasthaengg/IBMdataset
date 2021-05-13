str=input()
q=eval(input())
command=[]
replace=[]
numdata=[]
for i in range(q):
    x=input()
    if 'replace' in x:
        a,b,c,d=x.split()
        replace.append(d)
        numdata.append((int(b),int(c)))
    else:
        a,b,c=x.split()
        numdata.append((int(b),int(c)))
    command.append(a)
Re=iter(replace)
for i in range(q):
    if command[i]=='print':
        print(str[numdata[i][0]:numdata[i][1]+1])
    elif command[i]=='reverse':
        temp=str[numdata[i][0]:numdata[i][1]+1]
        str=str[:numdata[i][0]]+temp[::-1]+str[numdata[i][1]+1:]
    else:
        str=str[:numdata[i][0]]+next(Re)+str[numdata[i][1]+1:]