n=int(input())
ts = list(map(int,input().split()))
As = list(map(int,input().split()))
tr = [0]*n
ar = [0]*n
ct = 0
ca = 0
for i in range(n):
    if ct!=ts[i]:
        tr[i]=(ts[i],ts[i])
        ct=ts[i]
    else:
        tr[i]=(1,ts[i])
    if ca!=As[n-i-1]:
        ar[n-i-1]=(As[n-i-1],As[n-i-1])
        ca=As[n-i-1]
    else:
        ar[n-i-1]=(1,As[n-i-1])
#print(tr)
#print(ar)
ans=1
for i in range(n):
    if tr[i][0]==1 and ar[i][0]==1:
        ans=(ans*min(tr[i][1],ar[i][1]))%1000000007
    elif tr[i][0]==1 and ar[i][0]>1:
        if tr[i][1]<ar[i][1]:
            print(0)
            break
    elif tr[i][0]>1 and ar[i][0]==1:
        if tr[i][1]>ar[i][1]:
            print(0)
            break
    else:
        if tr[i][0]!=ar[i][0]:
            print(0)
            break
else:
    print(ans%1000000007)
