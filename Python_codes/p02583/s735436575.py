n=int(input())
l=list(map(int,input().split()))
l.sort()

cnt=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (l[i]==l[j] or l[j]==l[k] or l[k]==l[i]):
                continue
            if l[k]-l[j]-l[i]<0:
                cnt+=1

print(cnt)
