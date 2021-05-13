H,W=map(int, input().split())
A=[]
for i in range(H):
    a=list(map(int, input().split()))
    A.append(a)


ans=[]
count=0
for h in range(H):
    for w in range(W):
        if h%2==1:
            w=W-1-w
        if h==0 and w==0:
            px,py=0,0
            pre=0
            if A[h][w]%2==0:
                continue
            else:
                A[h][w]-=1
                pre=1
        else:
            if pre>0:
                A[h][w]+=pre
                pre=0
                ans.append([px+1,py+1,h+1,w+1])
                count+=1
            if A[h][w]%2==1:
                A[h][w]-=1
                pre=1
                px,py=h,w

#print(ans)
print(count)
for a in ans:
    print(*a)