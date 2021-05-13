from collections import deque
n, k, c = map(int, input().split())
s = list(map(lambda x: 1 if x == 'o' else 0, input()))
b_a = deque()
b_b = deque()
c_k = 0
for i in range(n-1, -1, -1):
    if c_k == 0 and s[i] == 1:
        b_a.append(i)
        c_k = c
    else:
        c_k = max(c_k-1, 0)
c_k = 0
for i in range(n):
    if c_k == 0 and s[i] == 1:
        b_b.append(i)
        c_k = c
    else:
        c_k = max(c_k-1, 0)

ans = list(set(b_a) & set(b_b))
ans.sort()
if len(ans) <= k:
    for i in ans:
        print(i+1)