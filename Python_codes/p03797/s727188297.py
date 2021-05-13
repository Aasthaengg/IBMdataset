S = list(map(int,input().split()))
N=S[0]
M=S[1]
N1=0
M1=0
count = 0

if 2*N<=M:
    count = N
    N1=0
    M1=M-2*N
    count+=M1//4
elif M<2*N:
    count += M//2
print(count)