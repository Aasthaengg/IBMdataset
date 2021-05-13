R, G, B, N = map(int, input().split())

cnt = 0
for r in range(N//R+1):
    Rr = R*r
    for g in range((N-Rr)//G+1):
        if (N-(Rr + G*g)) % B == 0:
            cnt += 1
print(cnt)