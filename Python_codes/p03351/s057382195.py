
a,b,c,d=map(int,input().split())

if (0<=abs(a-c)<=d) or (0<=abs(a-b)<=d and 0<=abs(b-c)<=d):
    print('Yes')

else:print('No')