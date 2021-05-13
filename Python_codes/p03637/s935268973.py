def mp2(k):
    kk=k
    mp=0
    while kk>=1:
        kr=kk%2
        if kr==0:
            kk=kk//2
            mp=mp+1
#            print(kk,kr,mp)
        else:
#            print(kk,kr,mp)
            return mp
    return mp
        

n=int(input())
a=list(map(int,input().split()))

cnt0=0
cnt1=0
cnt2=0
for i in range(n):
    m=min(2,mp2(a[i]))
    if m==0:
        cnt0=cnt0+1
    elif m==1:
        cnt1=cnt1+1
    elif m==2:
        cnt2=cnt2+1

#print(cnt0,cnt1,cnt2)

if cnt1==0:
    if cnt2>=cnt0-1:
        print("Yes")
    else:
        print("No")
else:
    if cnt2>=cnt0:
        print("Yes")
    else:
        print("No")
