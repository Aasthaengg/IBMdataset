N,K = map(int,input().split())

tmp = N // K

if N % K == 0:
    print(0)
else:
    print(1)