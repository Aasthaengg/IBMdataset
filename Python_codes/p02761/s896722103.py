N,M = map(int,input().split())
C = [-1] * (N + 1)
for i in range(M):
    s,c = map(int,input().split())
    if C[s] != -1 and C[s] != c:
        print(-1)
        exit(0)
    C[s] = c 
ans = ''
if N == 1:
    if C[1] == 0 or C[1] == -1:
        print(0)
    else:
        print(C[1])
    exit(0)
    
if C[1] == 0:
    print(-1)
    exit(0)
elif C[1] == -1:
    ans += '1'
else:
    ans += str(C[1])
    
for i in range(2,N+1):
    if C[i] == -1:
        ans += '0'
    else:
        ans += str(C[i])
print(ans)