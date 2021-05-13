H,W,K=map(int,input().split())
A = []
B = []
for _ in range(H):
    A.append(input())
for i in range(H):
    B.append(list(A[i]))

sum=0
X = 2**H-1
Y = 2**W-1

x=X
while(x):
    y=Y
    while(y):
        S=0
        for i in range(H):
            for j in range(W):
                if B[i][j]=='#' and (1<<i)&x and (1<<j)&y:
                    S+=1
        if S==K:
            sum+=1
        y = (y-1) & 2**W-1
    x = (x-1) & 2**H-1
print(sum)