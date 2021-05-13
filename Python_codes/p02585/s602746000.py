import sys

n,k=map(int,input().split())

p=list(map(int,input().split()))
c=list(map(int,input().split()))

check=[0 for i in range(n)]

if max(c)<0:
    print(max(c))
    sys.exit()

ans=0

for i in range(n):
    if check[i]==0:
        cnt=0
        check[i]=1
        li=[i]
        pc=p[i]-1
        while pc!=i:
            check[pc]=1
            li.append(pc)
            pc=p[pc]-1
        sumli=0
        for j in li:
            sumli+=c[j]
        add=0
        ki=k
        if k>len(li):
            if sumli>0:
                ki=(ki-1)%len(li)+1
                add=sumli*((k-ki)//len(li))
            else:
                ki=len(li)
        for w in range(1,ki+1):
            sumwmax=0
            sumw=0
            for j in range(w):
                sumw+=c[li[j]]
            for j in range(len(li)):
                sumw=sumw-c[li[j]]+c[li[(j+w)%len(li)]]
                sumwmax=max(sumw,sumwmax)
            cnt=max(cnt,sumwmax)
        ans=max(ans,cnt+add)

print(ans)