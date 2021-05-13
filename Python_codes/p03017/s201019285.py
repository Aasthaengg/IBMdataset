n,a,b,c,d = map(int,input().split())
s = input()
a,b,c,d = a-1,b-1,c-1,d-1

def move(a,s):
    ar = a
    while(ar<n-2):
        if(s[ar+2]=='.'):
            ar += 2
        elif(s[ar+1]=='.'):
            ar +=1
        else:
            break
    if(ar!=n-1):
        ar+=(s[ar+1]=='.')
    return ar

def pr_end(x):
    if(x):
        print('Yes')
    else:
        print('No')
    exit()

ar = move(a,s)
br = move(b,s)

if(c<d):
    if(c<=ar)&(d<=br):
        pr_end(1)
    else:
        pr_end(0)

for i in range(b-1,d):
    if(s[i:i+3] =='...'):
        if(c<=ar)&(d<=br):
            pr_end(1)
        else:
            pr_end(0)

pr_end(0)