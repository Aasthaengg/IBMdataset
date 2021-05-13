import sys,math
input = sys.stdin.readline

N,M = list(map(int,input().split()))
S = input().rstrip()
T = input().rstrip()

L = N*M//math.gcd(N,M)

sn = L//M
tm = L//N

for i in range(N//sn):
    if S[i*sn] == T[i*tm]:
        continue
    else:
        print(-1)
        exit()
print(L)
    
