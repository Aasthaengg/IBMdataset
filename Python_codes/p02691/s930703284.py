from collections import defaultdict
N = int(input())

A = list(map(int, input().split()))

dic = defaultdict(int)

ans = 0

for i in range(N):
    t = i - A[i]
    ans += dic[t]
    dic[i+A[i]] += 1

print(ans)
