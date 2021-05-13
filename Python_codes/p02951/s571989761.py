a,b,c = map(int,input().split())
s = a-b

c -= s
if(c<0):
    print(0)
else:
    print(c)
