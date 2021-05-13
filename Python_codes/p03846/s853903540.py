N = int(input())
A = list(map(int,input().split()))
T = [0]*N
for i in range(N):
    T[A[i]]+=1
flag = 0
if N%2==1:
    for i in range(N):
        if i==0 and T[i]!=1:
            flag = 1
        elif i%2==0 and i>=2 and T[i]!=2:
            flag = 1
elif N%2==0:
    for i in range(N):
        if i%2==1 and T[i]!=2:
            flag = 1
if flag==1:
    print(0)
else:
    if N%2==1:
        print(pow(2,(N-1)//2,10**9+7))
    else:
        print(pow(2,N//2,10**9+7))