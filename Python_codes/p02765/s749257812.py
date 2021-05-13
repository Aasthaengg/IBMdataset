N,R = map(int,input().split())

if N<10:
    x=R+(100*(10-N))
    print(x)
    exit()
print(R)