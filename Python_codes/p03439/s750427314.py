n=int(input())
q=lambda i:input('%d\n'%i)
i=0
j=n-1
a=q(i)
b=q(j)
while 1:
    if j-i<2:
        q(i)
        q(j)
    k=(j-i)//2+i
    c=q(k)
    if(k-i)%2and a==c or not(k-i)%2and a!=c:
        j=k
    else:
        a=c
        i=k