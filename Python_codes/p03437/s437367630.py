x, y = map(int, input().split())

if x==y or x%y==0:
    print(-1)
else:
    for i in range(2, 10**9):
        if (x*i)%y!=0:
            print(x*i)
            import sys
            sys.exit()
    print(-1)