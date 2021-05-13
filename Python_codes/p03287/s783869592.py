n,m=map(int,input().split())
a=list(map(int,input().split()))

cnt=0
dic={}
dic[0]=1
aaa=0
for aa in a:
    aaa+=aa

    if aaa%m in dic:
        cnt+=dic[aaa%m]
        dic[aaa%m]+=1
    else:
        dic[aaa%m]=1
            #print(aaa,aa,aaa%m,dic)
    #print(dic)
print(cnt)

