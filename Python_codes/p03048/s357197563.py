R,G,B,N = map(int,input().split())
res = 0
for i in range(N//R + 1):
    for j in range(N//G + 1):
        if i*R + j*G > N: # はそもそもむり
            continue
        k = (N - R*i - G*j)
        if k % B != 0: # その倍数じゃないと無理
            continue
        res += 1
print(res)
