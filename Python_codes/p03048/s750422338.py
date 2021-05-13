R,G,B,N = map(int,input().split())
cnt = 0
for i in range(N//R+1):
    M = N-R*i
    for j in range(M//G+1):
        L = M-G*j
        if L % B == 0:
            cnt += 1

print(cnt)