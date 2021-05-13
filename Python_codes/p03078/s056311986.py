X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

AB = [0]*X*Y
i = 0
for a in A:
    for b in B:
        AB[i] = a + b
        i += 1
AB.sort(reverse=True)

ans = [0]*min(K, len(AB))*Z
i, j = 0, 0
for i in range(min(K, len(AB))):
    for c in C:
        ans[j] = AB[i] + c
        j += 1
ans.sort(reverse=True)

for i in range(K):
    print(ans[i])