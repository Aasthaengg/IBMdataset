v=pow(10,9)+7
arr=[]
inp = list(map(int,input().split()))
row=inp[0]
col=inp[1]
for i in range(row):
    s=input()
    arr.append(s)
ans=[[0 for i in range(col)]for j in range(row)]
for i in range(col):
    if arr[0][i]=='#':
        break
    else:
        ans[0][i]=1
for i in range(row):
    if arr[i][0]=='#':
        break
    else:
        ans[i][0]=1
for i in range(1,row):
    for j in range(1,col):
        if arr[i][j]=='#':
            continue
        else:
            ans[i][j]=(ans[i-1][j]+ans[i][j-1])%v
print (ans[-1][-1])