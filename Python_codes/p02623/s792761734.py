n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sa=[]
sma=0
for i in range(n):
    sma+=a[i]
    sa.append(sma)
sb=[]
smb=0
for i in range(m):
    smb+=b[i]
    sb.append(smb)
import bisect
lain=bisect.bisect_right(sa,k)-1
if lain<0:
    sm=0
else:
    sm=sa[lain]
stin=bisect.bisect_right(sb,k-sm)-1

if lain<0:
    print(stin+1)
    exit()
if stin>=m-1:
    print(lain+1+m)
    exit()
am=lain+1+stin+1
mx=am
for i in range(lain,-1,-1):
    sm-=a[i]
    am-=1
    while sm+sb[stin+1]<=k:
        stin+=1
        am+=1
        if stin>=m-1:
            print(max(mx,am))
            exit()
    mx=max(mx,am)
print(mx)
    
