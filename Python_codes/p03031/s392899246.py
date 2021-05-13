N, M = map(int,input().split())

switch = []
for _ in range(M):
    S = list(map(int,input().split()))
    switch.append(S[1:])

P = list(map(int,input().split()))

ans = 0
for bits in range(1<<N):
    flag = True

    for i in range(M):
        cnt = 0
        for s in switch[i]:
            if(bits>>(s-1) & 1):
                cnt += 1

        if cnt % 2 != P[i]:
            flag = False
    
    if flag: ans += 1

print(ans)