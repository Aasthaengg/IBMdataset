import pprint
H,W,K=map(int,input().split())
table=[list(input()) for _ in range(H)]
ans=[[0 for _ in range(W)] for _ in range(H)]
l= [0]*W
begin=0
end=0
cnt=1
while end<H:
    l2=[0]*W
    flag=0
    for i in range(W):
        l2[i]=l[i]
    for i in range(W):
        if (table[end][i]=="#")and(l[i]==1):
            l=l2
            flag=1
            break
        elif (table[end][i]=="#"):
            l[i]=1
    if flag==0:
        end=end+1
    else:
        lr=[]
        st=0
        for i in range(W):
            if l[i]==1:
                en=i+1
                lr.append([st,en])
                st=en
        lr[len(lr)-1][1]=W
        #print(begin,end,l,lr)
        for i in range(len(lr)):
            left=lr[i][0]
            right=lr[i][1]
            for j in range(begin,end):
                for k in range(left,right):
                    ans[j][k]=cnt
            cnt=cnt+1
        begin=end
        l=[0]*W
lr=[]
st=0
for i in range(W):
    if l[i]==1:
        en=i+1
        lr.append([st,en])
        st=en
lr[len(lr)-1][1]=W
#print(begin,end,l,lr)
for i in range(len(lr)):
    left = lr[i][0]
    right = lr[i][1]
    for j in range(begin, end):
        for k in range(left, right):
            ans[j][k] = cnt
    cnt = cnt + 1
for i in range(H):
    print(*ans[i])


