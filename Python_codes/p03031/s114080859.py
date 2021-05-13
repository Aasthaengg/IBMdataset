N,M = map(int, input().split())
S = [[]for i in range(M)]
for i in range(M):
    k_s = list(map(int, input().split()))
    for j in range(len(k_s)-1):
        S[i].append(k_s[j+1])
p = list(map(int, input().split()))
Answer = 0
#print(S)

for i in range(2 ** N):
    switch = [0]*N
    for j in range(N):  # このループが一番のポイント
        a = 0
        if ((i >> j) & 1):
            a = 1

        switch[j] = a


    flag = True
    for j in range(M):
        Sum = 0
        for k in range(len(S[j])):
            #print(j,k)
            Sum += switch[S[j][k]-1]

        if (Sum%2) != p[j]:
            break

        if j == M-1:
            Answer += 1

print(Answer)
