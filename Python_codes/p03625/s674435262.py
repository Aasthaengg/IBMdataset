from collections import Counter

N=int(input())
A=list(map(int,input().split()))
c=Counter(A)
c=c.most_common()
c.sort(reverse=True,key=lambda x:x[0])
cnt=0
H=0
W=0
for i in range(len(c)):
    if cnt==0 and c[i][1]>=4:
        H,W=c[i][0],c[i][0]
        print(H*W)
        exit()
    elif cnt==0 and c[i][1]>=2:
        H=c[i][0]
        cnt+=1
    elif cnt==1 and c[i][1]>=2:
        W=c[i][0]
        print(H*W)
        exit()
print(H*W)