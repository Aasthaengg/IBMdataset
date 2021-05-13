n,k=map(int,input().split())
if k > (n-1)*(n-2)//2 :
    print(-1)
else:
    print((n-1)*(n-2)//2 - k+n-1)
    for i in range(2,n+1):
        print("1 "+str(i))
    res = []
    for i in range(2,n):
        for j in range(i+1,n+1):
            res.append(str(i)+" "+str(j))
    print("\n".join(res[:((n-1)*(n-2)//2) - k]))