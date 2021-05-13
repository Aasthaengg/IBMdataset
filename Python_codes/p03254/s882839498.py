n,x=map(int,input().split())
A=sorted(list(map(int,input().split())))
for i in range(n):
    if x-A[i]>=0:
        x=x-A[i]
    else:
        print(i)
        exit()
if x==0:print(n)
else:print(n-1)