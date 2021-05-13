N=int(input())
A=list(map(int,input().split()))

odd=0
for i in range(0,N):
    if A[i]%2==1:
        odd=odd+1

if odd%2==1:
    print('NO')
else:
    print('YES')
