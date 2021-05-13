X,Y=map(int,input().split())

for i in range(2,10**5):
    if (i*X)%Y!=0:
        print(i*X)
        break
else:
    print(-1)