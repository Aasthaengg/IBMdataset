import collections

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

d = collections.Counter(D)
t = collections.Counter(T)

ans = 'YES'
t_v = list(t.values())
t_k = list(t.keys())
for i in range(len(t)):
    if t_v[i] > d[t_k[i]]:
        ans = 'NO'

print(ans)