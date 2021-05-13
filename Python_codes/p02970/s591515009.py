n,d=map(int,input().split())
for i in range(20):
    if i*((d-1)*2+3)>=n:
        print(i)
        exit()