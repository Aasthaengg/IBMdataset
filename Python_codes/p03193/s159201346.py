a,b,c=map(int,input().split())
x = 0
for i in range(a):
    A,B=map(int,input().split())
    if A>=b and B>=c:
        x=x+1
    else:
        x=x
print(x)
