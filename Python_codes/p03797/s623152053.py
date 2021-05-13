N,M = map(int, input().split())
if M-2*N < 0:
    ret = M//2
else:
    M = M-2*N
    ret = N
    ret += M//4
    
print(ret)