N,M = map(int,input().split())
S =[0]*M
for i in range(M):
    k,*s = map(int,input().split())
    S[i] = s

P = list(map(int,input().split()))
ans = 0
for num in range(1<<N):
    Light = [0] * N
    count = 0
    for i in range(N):
        bit = num>>i & 1
        if bit:
            Light[i] = 1
    for i,s in enumerate(S):
        light_count = 0
        p = P[i]
        for si in s:
            if Light[si-1]:
                light_count += 1
        if light_count % 2 == p:
            count+=1
    if count == M:
        ans += 1

print(ans)












