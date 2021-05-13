N,M = map(int,input().split())

if N != 0 and M != 0:
    x = N*(N-1)/2+M*(M-1)/2
elif N == 0:
    x = M*(M-1)/2
else:
    x = N*(N-1)/2

print(int(x))