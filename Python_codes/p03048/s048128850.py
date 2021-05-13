R,G,B,N = map(int,input().split())
cnt = 0
for r in range(N//R+1):
    for g in range(N//G+1):
        n = N-r*R-g*G
        if n>=0 and n%B==0:
            cnt += 1
print(cnt)