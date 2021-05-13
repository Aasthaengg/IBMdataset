N,M=map(int,input().split())
twice=(N==M)+(abs(N-M)<=1)

n=m=1
while N:
    n*=N
    n%=10**9+7
    N-=1

while M:
    m*=M
    m%=10**9+7
    M-=1

print((n*m*twice)%(10**9+7))