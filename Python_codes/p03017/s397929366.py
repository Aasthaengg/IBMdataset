n,a,b,c,d = map(int, input().split())
a-=1
b-=1
c-=1
d-=1
s = input()
s+='X'
ch=1
v=[]
st=[]
if s[0]=='#':
    v.append((0,0))
for i in range(1,n+1):
    if s[i]==s[i-1]:
        ch+=1
    else:
        v.append((ch,i-ch))
        ch=1
judge=[]
for i in range(len(v)):
    if i%2==1:
        x,y=v[i]
        if x>=2 and ((a < y and y < c) or (b < y and y < d)):
            print('No')
            exit()
    else:
        x,y=v[i]
        if x>=3:
            judge.append((y,y+x-1))
check=1
if (a<b and d<c) or (b<a and c<d):
    check = 0
    while judge:
        t1,t2=judge.pop()
        if t2>a and t2>b and t1<c and t1<d:
            check = 1
if check == 1:
    print('Yes')
else:
    print('No')
