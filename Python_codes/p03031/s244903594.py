N,M = map(int,input().split())
Connect = [0] * M
for i in range(M):
    k, *Connect[i] = map(int,input().split())
P = list(map(int,input().split()))
Switch = [0] * N
ans = 0
for i in range(1<<N):
    for j in range(N):
        bit = i>>j & 1
        Switch[j] = bit
    flag = True
    for l in range(M):
        count = 0
        for c in Connect[l]:
            if Switch[c-1]:
                count+=1
        if not P[l] == count % 2:
            flag = False
    if flag:
        ans += 1

print(ans)





