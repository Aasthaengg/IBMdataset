X,Y = map(int,input().split())
for i in range(1,10**6):
    if((X*i) % Y != 0):
        print(X*i)
        exit()
print(-1)
