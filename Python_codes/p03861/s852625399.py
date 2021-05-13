a,b,x = map(int,input().split())
if a%x!=0:
    temp = a%x
    a += x-temp
if a>b:
    print(0)
elif a==b:
    print(1)
else:
    temp = (b-a)//x
    print(temp+1)