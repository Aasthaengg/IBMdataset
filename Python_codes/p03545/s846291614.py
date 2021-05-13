s=input()
A=[]
d=s[0]
for i in range(2**(len(s)-1)):
    v=[]
    for j in range(len(s)-1):
        if ((i>>j)&1):
            v.append('+')
        else:
            v.append('-')
    A.append(v)

for i in range(len(A)):
    c=int(s[0])
    for j in range(3):
        if A[i][j]=='+':
            c+=int(s[j+1])
        else:
            c-=int(s[j+1])
    if c==7:
        for j in range(3):
            d+=A[i][j]+s[j+1]
        print(d+'=7')
        exit()