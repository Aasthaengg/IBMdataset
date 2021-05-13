import math
N=int(input())

ans=10**10

for i in range(1,int(N/2)+1):
    j = N-i
    A = list(map(int,str(i)))
    B = list(map(int,str(j)))

    X = sum(A) + sum(B)

    if ans > X:
        ans = X
print(ans)
