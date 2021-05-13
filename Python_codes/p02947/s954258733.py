import collections
N = int(input())
S = [sorted(input()) for _ in range(N)]
Ssrt = []
for s in S:
    s = ''.join(s)
    Ssrt.append(s)
cnt = collections.Counter(Ssrt)
ans = 0
for i in cnt.keys():
    if cnt[i] >= 2:
        ans += cnt[i]*(cnt[i]-1)//2
print(ans)
