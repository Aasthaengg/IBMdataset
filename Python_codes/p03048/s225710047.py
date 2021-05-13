R,G,B,N = map(int,input().split())
cnt = 0
for r in range(N//R+1):
    nR = N-r*R
    for g in range(0,nR//G+1):
        nG = nR-g*G
        if nG%B==0:
            cnt += 1
print(cnt)
