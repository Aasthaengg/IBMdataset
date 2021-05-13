N, K = map(int, input().split())
RSP = list(map(int, input().split()))
T = list(input())
rsp = ['r', 's', 'p']
for i in range(N-K):
    if T[i] == T[i+K]:
        T[i+K] = 0
print(sum(RSP[i]*T.count(rsp[(i+1)%3]) for i in range(3)))
