n = int(input())
t,x,y = 0,0,0

for i in range(n):
    T,X,Y = map(int,input().split())
    dt,dx,dy = T-t,abs(X-x),abs(Y-y)
    if dt - (dx + dy) < 0 or (dt - (dx + dy))%2 == 1:
        print("No")
        exit()
    t,x,y = T,X,Y

print("Yes")