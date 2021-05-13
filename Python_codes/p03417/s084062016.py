import sys
input = sys.stdin.readline
N,M=map(int,input().split())
if N==2 or M==2:
    print(0)
    exit()
if N==1 and M==1:
    print(1)
    exit()
if N==1 or M==1:
    print(max(N,M)-2)
    exit()
print((N-2)*(M-2))
