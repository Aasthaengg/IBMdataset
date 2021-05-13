n=int(input())
h=list(map(int,input().split()))

p=max(h)
cnt=[]
ct=0


for i in range(p):
    ct=0
    for j in range(len(h)-1):
        if h[j]==p-i:
            if h[j]==h[j+1]:
                h[j]-=1
                if j==len(h)-2:
                    ct+=1
                    h[j+1]-=1
            else:
                ct+=1
                h[j]-=1
        if j==(len(h)-2):
            if h[j]!=p-i and h[j+1]==p-i:
                h[j+1]-=1
                ct+=1
    cnt.append(ct)
    #print(h,ct)


k=sum(cnt)
if len(h)==1:
    print(h[0])
else:
    print(k)

