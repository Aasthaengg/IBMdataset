N,M = map(int,input().split())
if N ==1 and M ==1:
    print(0)
elif N ==1 and M != 1:
    print(int(M*(M-1)/2))
elif N != 1 and M ==1:
    print(int(N*(N-1)/2))
else:    
    a = N*(N-1)
    b = M*(M-1)
    print(int((a+b)/2))