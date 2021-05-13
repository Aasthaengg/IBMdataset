n=int(input())
ans = []
c = 1
while True:
    c+=1
    res=(1+c)*c/2
    if res>=n:
        diff=res-n
        for i in range(1,c+1):
            if i==diff:
                continue
            print(i)
        break
