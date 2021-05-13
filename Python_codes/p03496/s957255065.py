N=int(input())
a=[int(i) for i in input().split()]
argM=0
argm=0
for i in range(N):
    if a[argM]<a[i]:
        argM=i
    if a[argm]>a[i]:
        argm=i
if a[argM]<=0:
    print(N-1)
    for i in list(range(N-1))[::-1]:
        a[i]+=a[i+1]
        print(i+2,i+1)
elif a[argm]>=0:
    print(N-1)
    for i in range(N-1):
        a[i+1]+=a[i]
        print(i+1,i+2)
else:
    L=[]
    if a[argM]+a[argm]>=0:
        for i in range(N):
            if i==argM:
                continue
            L.append([argM+1,i+1])
            a[i]+=a[argM]
        for i in range(N-1):
            a[i+1]+=a[i]
            L.append([i+1,i+2])
        print(len(L))
        for p in L:
            print(p[0],p[1])
    else:
        for i in range(N):
            if i==argm:
                continue
            L.append([argm+1,i+1])
            a[i]+=a[argm]
        for i in list(range(N-1))[::-1]:
            a[i]+=a[i+1]
            L.append([i+2,i+1])
        print(len(L))
        for p in L:
            print(p[0],p[1])
#print(a)
