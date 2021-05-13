import math
N = int( input())
As  = [int(input())for _ in  range(N)]
ans = 0
for i in range(N):
    if As[i] > i or As[i] - As[i - 1] > 1:
        ans = -1
        break

    else:
        if As[i] == As[i -1] + 1:
            ans += 1
        else:
            ans += As[i]

print(ans)
