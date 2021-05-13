n=int(input())
a=list(map(int, input().split()))
for i in range(32):
    x=2**i
    res=0
    for j in a:
        if j%x !=0:
            res=1
    if res==1:
        print(i-1)
        break

