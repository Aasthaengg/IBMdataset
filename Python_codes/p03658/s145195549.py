N,K = list(map(int, input().split()))
L = list(map(int, input().split()))

dct = sorted(L, reverse=True)

ans = []

for i in range(K):
    ans.append(dct[i])

print(sum(ans))