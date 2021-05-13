# https://takeg.hatenadiary.jp/entry/2019/11/22/212816
# https://drken1215.hatenablog.com/entry/2019/10/20/032700

import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0

for a in range(N):
    for b in range(a+1, N):
        c = bisect.bisect_left(L, L[a] + L[b])
        # print(a, b, c)
        ans += max(c-(b+1), 0)
        # print(ans)

print(ans)
