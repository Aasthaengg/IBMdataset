N = int(input())
A = list(map(int,input().split()))
x = 1000
cnt = 0
flag = 0
for i in range(1,N):
    if flag==0 and A[i]-A[i-1]>0:
        cnt += x//A[i-1]
        x = x%A[i-1]
        flag = 1
    elif flag==0 and A[i]-A[i-1]<0:
        x += cnt*A[i-1]
        cnt = 0
        flag = -1
    elif flag==1 and A[i]-A[i-1]<0:
        x += cnt*A[i-1]
        cnt = 0
        flag = -1
    elif flag==-1 and A[i]-A[i-1]>0:
        cnt += x//A[i-1]
        x = x%A[i-1]
        flag = 1
if flag==1:
    x += cnt*A[N-1]
    cnt = 0
print(x)