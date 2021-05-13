n=int(input())
b=list(map(int,input().split()))
num=[]
for i in range(n):
    num.append([b[i],0]) #0はまだ残ってる　１は取り除いた
flag=True
ans=[]
remove=0 #取り除いた数。
remove_sum=[0]*n
while flag and remove<=n-1:
    remove_ind=-1
    for i in range(n):
        if num[i][1]==0:
            if i-remove_sum[i]==num[i][0]-1:
                remove_ind=i
    if remove_ind!=-1:
        num[remove_ind][1]=1
        remove+=1
        ans.append(num[remove_ind][0])
        for j in range(remove_ind+1,n):
            remove_sum[j]+=1
    else: #取り除くものがなかった
        flag=False
if flag:
    ans=ans[::-1]
    for i in range(n):
        print(ans[i])
else:
    print(-1)