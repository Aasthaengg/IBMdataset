N, K = map(int,input().split())
L = list(map(int,input().split()))
L = sorted(L)[::-1]
s = 0
for i in range(K):
    s += L[i]
print(s)
