n,k=map(int,input().split())
m=(n-1)*(n-2)//2
if k>m:
    print(-1)
else:
    l=m-k
    lst=[]
    for i in range(1,n):
        lst.append([i,n])
    for i in range(1,n):
        for j in range(i+1,n):
            if l==0:
                break
            lst.append([i, j])
            l-=1
        else:
            continue
        break
    print(len(lst))
    for a,b in lst:
        print(a,b)