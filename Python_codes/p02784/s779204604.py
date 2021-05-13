h,n=map(int,input('').split(' '))
a=list(map(int,input('').split(' ')))
s=0
for i in range(n):
    s=s+a[i]

if s>=h:
    print('Yes')
else:
    print('No')