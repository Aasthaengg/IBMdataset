a, b, c, k = map(int,input().split())

if a==b==c:
    print(0)
    exit()
    
a_=b+c
b_=a+c
c_=a+b

if k==0:
    print(a-b)
elif k%2==0:
    print(a-b)
else:
    print(a_-b_)