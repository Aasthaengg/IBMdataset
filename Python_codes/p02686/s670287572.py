n = int(input())
left=[]
right=[]
for i in range(n):
    s = input()
    l = len(s)
    a=0
    b=0
    a1=0
    b1=0
    for j in range(l):
        if s[j]==')':
            a1+=1
        else:
            a1-=1
        a=max(a1,a)
    for j in range(l):
        if s[l-1-j]=='(':
            b1+=1
        else:
            b1-=1
        b = max(b1,b)
    if a>b:
        right.append((a,b))
    else:
        left.append((a,b))
right.sort(key = lambda x:x[1],reverse=True)
left.sort(key = lambda x:x[0])
all = left+right

if all[0][0]>0:
    print('No')
    exit()
st = all[0][1]
for i in range(1,n):
    st-=all[i][0]
    if st<0:
        print('No')
        exit()
    st+=all[i][1]
if st>0:
    print('No')
else:
    print('Yes')
