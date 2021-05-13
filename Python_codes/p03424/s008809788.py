
N = int(input())
S = list(input().split())

flag=[0]*4
for i in range(N):
    if S[i]=='P':
        flag[0]=1
    elif S[i]=='W':
        flag[1]=1
    elif S[i]=='G':
        flag[2]=1
    elif S[i]=='Y':
        flag[3]=1

if sum(flag)==4:
    print('Four')
else:
    print('Three')
