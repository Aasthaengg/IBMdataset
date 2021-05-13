k,t=map(int,input().split())
a=list(map(int,input().split()))
for i in range(t):
    a[i]=[a[i],i]
prev=-1
if t>1:
    for i in range(k):
        a.sort(reverse=True)
        if a[0][1]==prev:
            if a[1][0]==0:
                break
            else:
                a[1][0]-=1
                prev=a[1][1]
        else:
            a[0][0]-=1
            prev=a[0][1]
    print(a[0][0])
else:
    print(a[0][0]-1)