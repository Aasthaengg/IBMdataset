n,m = map(int, input().split())
x = n-sum(list(map(int, input().split())))

if x < 0: 
    print(-1)
else:
    print(x)
