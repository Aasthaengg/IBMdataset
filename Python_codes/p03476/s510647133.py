Q = int(input())

minl = 10**9
maxr = -1
ans_range = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans_range.append((l, r))

    if l < minl:
        minl = l
    if r > maxr:
        maxr = r

dp = [0] * ((maxr - minl) + 2)

import math
for u in range(minl, maxr+1,1):
    check = (u + 1) / 2

    if not float.is_integer(check) or check == 1:
        dp[u - minl + 1] = dp[u-minl]
        continue

    ok = True
    for y in range(2, int(math.sqrt(check))+1):
        if check % y == 0:
            ok = False
            break

    ok2 = True
    for z in range(2, int(math.sqrt(u))+1):
        if u % z == 0:
            ok2 = False
            break
    
    if ok and ok2:
        # print("found: ", u)
        dp[u - minl + 1] = dp[u-minl] + 1
    else:
        # print("u:", u)
        dp[u - minl + 1] = dp[u-minl]

# print(dp)
for ll, rr in ans_range:
    if ll == rr:
        ans = dp[rr-minl+1] - dp[rr-minl]
    else:
        ans = dp[rr-minl+1] - dp[ll-minl]
    print(ans)