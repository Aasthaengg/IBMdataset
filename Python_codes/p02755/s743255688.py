a,b=map(int,input().split())

st=.08
lt=.1
s=[]
l=[]

for i in range(1262):
    if a/st<=i<(a+1)/st:
        s.append(i)

for i in range(1262):
    if b/lt<=i<(b+1)/lt:
        l.append(i)

t=[]

for i in s:
    if i in l:
        t.append(i)

if not t:
    print('-1')
else:
    print(min(t))