x,y,z,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort(reverse=True);b.sort(reverse=True);c.sort(reverse=True)
ng = 10**12
ok = 0
def check(chk):
    cnt=0
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if a[i]+b[j]+c[k]<chk:
                    break
                cnt+=1
                if cnt>K:
                    return True
    return False
while ng-ok>1:
    if check((ok+ng)//2):ok=(ok+ng)//2
    else:ng=(ok+ng)//2
cnt=0
l=[]
for i in range(x):
        for j in range(y):
            for k in range(z):
                if a[i]+b[j]+c[k]<ok:
                    break
                l.append(a[i]+b[j]+c[k])
l.sort(reverse=True)
for i in range(K):print(l[i])