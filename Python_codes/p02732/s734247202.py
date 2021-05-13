N = int(input())
A = list(map(int,input().split()))

from collections import Counter
cnt = Counter(A)

ans = 0
for v in cnt.values():
    ans += v*(v-1)//2
for i in A:
    a = cnt[i]
    dif = a*(a-1)//2 - (a-1)*(a-2)//2
    print(ans-dif)