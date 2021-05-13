N=int(input())
a=list(map(int,input().split()))

cnt=1
flag=False
renzoku=[]
for i in range(N):
    if i==N-1:
        renzoku.append(cnt)
    elif a[i]==a[i+1]:
        cnt+=1
    else:
        flag=False
        renzoku.append(cnt)
        cnt = 1

cnt=0
for i in renzoku:
    if i==1:
        continue
    else:
        cnt+=i//2

print(cnt)