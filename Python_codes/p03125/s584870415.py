#abc118 a
a,b=map(int,input().split())
flag=False
if max(a,b)%min(a,b)==0:
    flag=True
if flag:
    print(a+b)
else:
    print(b-a)