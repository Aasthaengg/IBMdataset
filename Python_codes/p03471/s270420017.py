n,y=map(int,input().split())
for a in range(0, min(n, y // 10000)+1):
    for b in range(0, min(n, y // 5000)+1):
        c=n-a-b
        if c>=0 and a*10000+b*5000+c*1000==y:
            print(a,b,c)
            exit()
print(-1,-1,-1)