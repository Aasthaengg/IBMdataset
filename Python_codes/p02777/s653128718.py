x=input().split()
s=x[0]
t=x[1]
a,b=map(int,input().split())
u=input()
if s==u:
    print(a-1,b)
else:
    print(a,b-1)
