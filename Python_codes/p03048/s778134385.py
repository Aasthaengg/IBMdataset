#diverta2019 programming contest-B
R,G,B,n = map(int,input().split())
cnt = 0
for i in range(n//R + 1):
    for j in range(n - i*R + 1):
        c = n - (i*R + j*G)
        if c >= 0 and c%B == 0:
            cnt += 1
        else:
            pass
                
print(cnt)
