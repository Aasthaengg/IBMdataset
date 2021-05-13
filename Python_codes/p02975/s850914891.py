n=int(input())
l=list(map(int,input().split()))
count=0
for i in l:
    count^=i
flag=True
for j in l:
    if j!=j^count:
        flag=False
        break
if flag==True:
    print('Yes')
else:
    print('No')