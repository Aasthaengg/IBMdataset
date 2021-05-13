a,b,x=map(int,input().split())
a_p=a//x
b_p=b//x

if a%x==0:
    print(b_p-a_p+1)
else:
    print(b_p-a_p)