from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))

ca = Counter(A)
ca = sorted(ca.items(), key=lambda x:x[1], reverse=True)

ans = 0
for i in range(min(K, len(ca))):
    ans += ca[i][1]

print(N-ans)