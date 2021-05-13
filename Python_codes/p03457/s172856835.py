n=int(input())
x,y=0,0
t=0
for i in range(n):
    T,X,Y=map(int,input().split())
    if((T-t)>=(abs(X-x)+abs(Y-y)) and (T-t)%2==(abs(x-X)+abs(Y-y))%2):
        x=X
        y=Y
        t=T
    else:
        print("No")
        exit()
print("Yes")
