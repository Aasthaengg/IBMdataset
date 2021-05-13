import sys
input = sys.stdin.readline

N,M,K=list(map(int,input().split()))
for iN in range(N+1):
    for iM in range(M+1):
        tmp = (N-iN)*(iM)+(iN)*(M-iM)
        if tmp == K:
            print('Yes')
            exit()
print('No')
