a,b,c,d=map(int,input().split())
if ((abs(b-a)<=d)&(abs(c-b)<=d))|(abs(c-a)<=d):
    print("Yes")
else:
    print("No")