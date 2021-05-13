x,n = map(int,input().split())
if n>0:
    p = list(map(int,input().split()))

    tmp = -100
    diff = 10000000
    for i in range(0,102):
        if abs(x-i)<diff and i not in p:
            tmp = i
            diff = abs(x-i)
            
    print(tmp)
else:
    print(x)