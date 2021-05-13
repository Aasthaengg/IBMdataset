N,X = map(int,input().split())
L = list(map(int,input().split()))
C = 1
M = 0

for i in range(N):
    M = M + L[i]
    if M > X:
        print(C)
        exit(0)
    
    C = C + 1

print(C)