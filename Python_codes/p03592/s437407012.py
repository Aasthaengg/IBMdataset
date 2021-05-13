import math
N,M,K = map(int,input().split())
list = [0 for i in range(N*M+1)]
i = 0
while i <= M:
    k=0
    list[N*i]=1
    while k < N:
        list[N*i+(M-2*i)*k]=1
        k+=1
    i+=1
j = 0
while j <= N:
    l = 0
    list[M*j]=1
    while l < M:
        list[M*j+(N-2*j)*l]=1
        l+=1
    j+=1
if list[K] ==1:
    print("Yes")
else:
    print("No")