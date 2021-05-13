R,G,B,N = map(int,input().split())
cnt = 0
R_1 = N//R
for i in range(R_1+1):
    G_1 = (N - i*R)//G
    for j in range(G_1+1):
        if (N - i*R - j*G)%B == 0:
            cnt += 1
print(cnt)