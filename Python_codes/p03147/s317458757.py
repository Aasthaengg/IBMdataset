N = int(input())
h = list(map(int,input().split()))
h.append(0)

cnt=0
flg=1
#flg=0  #0開始  1終わり
while max(h)>0:
    # print('h:',h)
    for i in range(N+1):
        if h[i] >=1:
            flg=0
        elif flg==0 and h[i]==0:
            flg=1
            cnt+=1
    for j in range(N):
        h[j]-=1
        if h[j]<0:
            h[j]=0

print(cnt)

