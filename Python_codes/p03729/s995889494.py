A=list(map(str, input().split()))
a=['']*3
b=['']*10
tmp1=''
tmp2=''
p=0
for i in range(3):
    a[i]=list(A[i])
    if i!=0:
        tmp2=a[i][0]
    if tmp1!='':
        if tmp1!=tmp2:
            p=1
    a[i]=list(reversed(a[i]))
    b=list(a[i])
    tmp1=b[0]
if p==0:
    print('YES')
else:
    print('NO')
  
  
