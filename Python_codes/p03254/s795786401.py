n,x=map(int,input().split())
a=sorted(list(map(int,input().split())))
if x>sum(a):
    print(n-1)
    exit()
elif x==sum(a):
    print(n)
    exit()
for i in range(n):
    if a[i]>x:
        print(i)
        exit()
    else:
        x-=a[i]