N, K = map(int, input().split())
A = list(map(int, input().split()))

import collections
A_tuple = collections.Counter(A).most_common()[::-1]

if len(A_tuple) < K:
    print(0)
else:
    ans = 0
    for i in range(len(A_tuple)-K):
        ans += A_tuple[i][1]
    print(ans)