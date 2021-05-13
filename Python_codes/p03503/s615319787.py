N = int(input())

F = []
for i in range(N):
    tmp = list(map(int,input().split()))
    F.append(tmp)

P = []
for i in range(N):
    tmp = list(map(int,input().split()))
    P.append(tmp)

ans = -1e10
for bits in range(1<<10):
    if bits == 0: continue

    cnt = [0 for i in range(N)]
    for i in range(10):
        if not (bits>>i & 1): continue 

        for shop in range(N):
            if F[shop][i]: cnt[shop] += 1
    
    benefit = 0
    for shop in range(N):
        benefit += P[shop][cnt[shop]]
    
    ans = max(ans, benefit)

print(ans)