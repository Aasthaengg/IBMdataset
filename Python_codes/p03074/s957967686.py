N,K = map(int,input().split())
S = list(map(int,list(input())))
count01 = [[0,0 if S[0]==1 else 1]]

now = -1
count = 0
for i in range(0,N,1):
    if now == S[i]:
        count+=1
    else:
        if now != -1:count01.append([count,S[i-1]])
        now = S[i]
        count=1
count01.append([count,S[N-1]])

for i in range(1,len(count01),1):
    count01[i][0]+=count01[i-1][0]#累積和とする。区間[a,b]の和はruiseki[b]-ruiseki[a-1]

ans=0
for i in range(0,len(count01),1):
    if count01[i][1]==1:
        ans = max(ans,count01[min(i+2*K,len(count01)-1)][0]-count01[max(i-1,0)][0])
    else:
        ans = max(ans,count01[min(i+2*K-2,len(count01)-1)][0]-count01[max(i-1,0)][0])
print(ans)
