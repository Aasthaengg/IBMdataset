n = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
ans = 0
A.sort()
if n%2==1:
    st = 0
    for i in range(1,n):
        if i%2==1:
            st+=2
        if A[i]!=st:
            print(0)
            exit()
else:
    st =-1
    for i in range(0,n):
        if i%2==0:
            st+=2
        if A[i]!=st:
            print(0)
            exit()
print(pow(2,n//2,mod))
