n=int(input())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
c=sorted(list(map(int,input().split())))
ma=0
cntb=[0]*n
for i in range(n):
    if i>0:
        cntb[i]=cntb[i-1]
    while ma<n:
        if a[ma]<b[i]:
            cntb[i]+=1
            ma+=1
        else:
            break
mb=0
cntc=[0]*n
for i in range(n):
    if i>0:
        cntc[i]=cntc[i-1]
    while mb<n:
        if b[mb]<c[i]:
            cntc[i]+=cntb[mb]
            mb+=1
        else:
            break
print(sum(cntc))
