X, Y=map(int, input().split())
i=X+X
MAX=10 ** 18
 
if X%Y== 0:
    print(-1)
else:
    while i<MAX:
        if i%Y != 0:
            print(i)
            break
        i+=X