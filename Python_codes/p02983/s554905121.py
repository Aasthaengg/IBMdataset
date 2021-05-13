l,r=map(int,input().split())

minv = 3000

if r//2019!=(l-1)//2019:
    print(0)

else :
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            if minv > i*j%2019:
                minv = i*j%2019

    print(minv)

