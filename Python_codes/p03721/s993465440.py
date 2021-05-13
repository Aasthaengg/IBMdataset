N,K = list(map(int,input().split()))
AB = [list(map(int,input().split())) for _ in range(N)]
M = {}
for ab in AB:
    if ab[0] in M:
        M[ab[0]] += ab[1]
    else:
         M[ab[0]] = ab[1]
tmp = 0
keys = sorted(M.keys())
if M[keys[0]] >= K:
    print(keys[0])
    exit()
for i in range(1,len(keys)):
    M[keys[i]] = M[keys[i]]+M[keys[i-1]]
    if M[keys[i-1]] < K <= M[keys[i]]:
        print(keys[i])
        exit()