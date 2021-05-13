n,k=map(int,input().split())
a=list(map(int,input().split()))
plus,minus,zero = 0,0,0
for i in range(n):
    if a[i] > 0:
        plus += 1
    elif a[i] < 0:
        minus += 1
    else:
        zero += 1
if n==k:
    ans=1
    for i in range(n):
        ans*=a[i]
        ans=ans%(10**9+7)
    print(ans)
else:
    if k%2==1 and minus==n:
        a.sort(reverse=True)
        ans=1
        for i in range(k):
            ans*=a[i]
            ans=ans%(10**9+7)
        print(ans)
    else:
        l=[]
        for i in range(n):
            if a[i]>=0:
                fugou=1
            else:
                fugou=-1
            l.append((abs(a[i]),fugou))
        l.sort(reverse=True)
        ans=1
        hu=1
        for i in range(k):
            ans*=l[i][0]
            ans=ans%(10**9+7)
            hu*=l[i][1]
        if hu==1:
            print(ans)
        elif ans==0:
            print(0)
        else:
            ss,sh,ts,th=-1,-1,-1,-1
            for i in range(k)[::-1]:
                if l[i][1]>0:
                    ss=l[i][0]
                    break
            for i in range(k)[::-1]:
                if l[i][1]<0:
                    sh=l[i][0]
                    break
            for i in range(k,n):
                if l[i][1]>0:
                    ts=l[i][0]
                    break
            for i in range(k,n):
                if l[i][1]<0:
                    th=l[i][0]
                    break
            if ss>0 and sh>0 and ts>0 and th>0:
                if th*sh>=ts*ss:
                    ans=(ans*pow(ss,10**9+5,10**9+7)*th)%(10**9+7)
                else:
                    ans=(ans*pow(sh,10**9+5,10**9+7)*ts)%(10**9+7)
                print(ans)
            else:
                if th>0 and ss>0:
                    ans=(ans*pow(ss,10**9+5,10**9+7)*th)%(10**9+7)
                else:
                    ans=(ans*pow(sh,10**9+5,10**9+7)*ts)%(10**9+7)
                print(ans)