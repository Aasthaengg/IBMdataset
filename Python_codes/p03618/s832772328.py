from collections import defaultdict

A = list(input())
N = len(A)

dic = defaultdict(int)

tmp = 0
for a in A:
    tmp += dic[a]
    dic[a] += 1

ans = N * (N - 1)//2 + 1 - tmp

print (ans)