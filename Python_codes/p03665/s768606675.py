N,P=map(int,input().split())
A=list(map(int,input().split()))
x,y=1,0
for a in A:
    if a%2:
        x,y=x+y,x+y
    else:
        x,y=x*2,y*2
print(y if P else x)