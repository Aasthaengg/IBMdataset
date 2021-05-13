from collections import defaultdict
A = input()
N = len(A)
ans = N * (N + 1) // 2
dic = defaultdict(int)
for i in range(N):
    dic[A[i]] += 1

for k in dic.values():
    ans -= k * (k + 1) // 2

print(ans + 1)
