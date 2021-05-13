X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# A+Bの上位K個
tmp = []
for a in A:
    for b in B:
        tmp.append(a + b)
tmp.sort(reverse=True)
tmp = tmp[:K]

ans = []
for ab in tmp:
    for c in C:
        ans.append(ab + c)
ans.sort(reverse=True)

for i in range(K):
    print(ans[i])
