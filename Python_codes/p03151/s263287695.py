N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
aff = [0]*N

if sum(A) < sum(B):
    print(-1)
else:
    need = 0
    ans = 0
    for i in range(N):
        aff[i] = A[i] - B[i]
    
    aff = sorted(aff)
    affrev = aff[::-1]
    
    for i in range(N):
        if aff[i] < 0:
            ans += 1
            need -= aff[i]
        else:
            break
    
    j = 0
    while need > 0:
        need -= affrev[j]
        ans += 1
        j += 1
    
    print(ans)   