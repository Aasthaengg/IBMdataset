from collections import defaultdict
N = int(input())
li = [int(x) for x in input().split()]
Q = int(input())

d = defaultdict(int)

for i in li:
    d[i] += 1

ans = sum(li)
for i in range(Q):
    B, C = map(int, input().split())
    ans += (C - B) * d[B]
    d[C] += d[B]
    d[B] = 0
    print(ans)
