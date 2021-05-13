from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

table = defaultdict(int)
ans = 0
for a in A:
    table[a] += 1
    ans += a

for _ in range(Q):
    B, C = map(int, input().split())
    diff = table[B] * (C - B)
    table[C] += table[B]
    table[B] = 0
    ans += diff
    print(ans)
