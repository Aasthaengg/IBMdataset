h,w,m=map(int,input().split())
HW=[list(map(lambda x:int(x)-1,input().split())) for _ in range(m)]

H,W=[0]*h,[0]*w
for i,j in HW:
    H[i] +=1
    W[j] +=1

max_h,max_w=max(H),max(W)
ans=max_h+max_w
cnt=H.count(max_h)*W.count(max_w)
for i,j in HW:
    if H[i]==max_h and W[j]==max_w:
        cnt -=1
print(ans if cnt!=0 else ans-1)