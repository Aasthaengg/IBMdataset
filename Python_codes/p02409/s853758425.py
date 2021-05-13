ls = [[[0 for i in range(10)] for j in range(3)]for s in range(4)]
n = int(input())
for g in range(0,n):
    b,f,r,v = map(int,input().split())
    ls[b-1][f-1][r-1] += v
for k in range(0,4):
    if k == 0:
        pass
    else:
        print("####################")
    for z in range(0,3):
        lis = ""
        for s in range(0,10):
            lis += " "+str(ls[k][z][s])
        print(lis)