N,K = (int(i) for i in input().split())
n = [i for i in range(1,N+1)]
ans = []
for i in range(len(n)-K+1):
    tmp = []
    for j in range(K):
        tmp.append(n[j+i])
    ans.append(tmp)
print(len(ans))
