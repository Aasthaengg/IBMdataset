N=int(input())
info1=list(map(int,input().split()))
info2=list(map(int,input().split()))
ans=0
if info1[-1]!=info2[0]: #お互いの最高記録が一致していないのは矛盾
    print(ans)
else:
    a=[[0,info1[0]]]
    highest=info1[0]
    for i in range(1,N):
        if highest<info1[i]:
            highest=info1[i]
            a.append([0,info1[i]])
        else:
            a.append([1,highest])
    b=[[0,info2[-1]]]
    highest=info2[-1]
    for i in range(1,N):
        if highest<info2[-(i+1)]:
            highest=info2[-(i+1)]
            b.append([0,info2[-(i+1)]])
        else:
            b.append([1,highest])
    flag=True
    c=[]
    for i in range(N): #二つの範囲を組み合わせる
        if a[i][0]==0 and b[-(i+1)][0]==0:
            if a[i][1]==b[-(i+1)][1]:
                c.append([0,a[i][1]])
            else:
                flag=False
                break
        elif a[i][0]==1 and b[-(i+1)][0]==1:
            c.append([1,min(a[i][1],b[-(i+1)][1])])
        else:
            if a[i][0]==0:
                if a[i][1]<=b[-(i+1)][1]:
                    c.append([0,a[i][1]])
                else:
                    flag=False
                    break
            else:
                if b[-(i+1)][1]<=a[i][1]:
                    c.append([0,b[-(i+1)][1]])
                else:
                    flag=False
                    break
    if flag:
        mod=10**9+7
        ans=1
        for i in range(N):
            if c[i][0]==1:
                ans=(ans*c[i][1])%mod
        print(ans)
    else:
        print(0)