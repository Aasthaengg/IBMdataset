N = int(input())
a = [int(input()) for x in range(N)]

import math

cnt = 0
for i in range(N) :
    cnt += 1
    if a[i] == 2 :
        continue
    else :
        for j in range(2, int(math.sqrt(a[i])) + 1) :
            if a[i] % 2 == 0 :
                cnt -= 1
                break
            if a[i] % j == 0 :
                cnt -= 1
                break
            
print(cnt)
