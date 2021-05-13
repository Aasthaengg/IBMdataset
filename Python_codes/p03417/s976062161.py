N,M = map(int,input().split())
ans = N*M
if N==1 and M==1:
    print(1)
    exit()
if N < 3 and M < 3:
    print(0)
    exit()
#偶数回操作が行われるもの
even = 0
#奇数回操作が行われるもの
odd = 0
#答えはoddの値
if N<=M:
    if N==1:
        s = 2*N
        print(ans-s)
    else:
        s = 2*N+2*(M-2)
        print(ans-s)
else:
    if M==1:
        s = 2*M
        print(ans-s)
    else:
        s = 2*M+2*(N-2)
        print(ans-s)