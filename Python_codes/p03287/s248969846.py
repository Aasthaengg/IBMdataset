from collections import Counter
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = [A[0] % M]
for i in range(N-1):
    B.append((B[-1]+A[i+1])%M)
count = Counter(B)
count[0] += 1
ans = 0
for i in count.values():
    ans += i * (i - 1) // 2
print(ans)