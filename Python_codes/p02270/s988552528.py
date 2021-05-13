import sys
import math

def is_capable(n, k, w, P):
    track = 0
    cnt = 0
    i = 0

    while cnt < k:
        if i == n:
            return True

        if track + w[i] > P:
            track = 0
            cnt += 1
        else:
            track += w[i]
            i += 1

    return False
    pass

# ??\?????¨
n, k = map(int, sys.stdin.readline().split())
w = []
for i in range(n):
    w.append(int(sys.stdin.readline().strip()))

'''
print(n,k)
print(w)
'''

# ????????¨

if k == 1:
    ans = sum(w)
    print(ans)
elif n == 1:
    ans = w[0]
    print(ans)
else:
    max_p = sum(w)
    min_p = math.ceil(max_p / k) - 1

    # print(max_p, min_p)
    # sys.exit(0)

    capable = {min_p:False, max_p:True}

    # sys.exit(0)
    
    bottom = min_p
    top = max_p

    while bottom < top:
        mid = (bottom + top) // 2

        if mid not in capable:
            capable[mid] = is_capable(n, k, w, mid)

        if capable[mid] == True:
            if (mid - 1) not in capable:
                capable[mid - 1] = is_capable(n, k, w, mid - 1)

            if capable[mid - 1] == False:
                ans = mid
                break
            else:
                top = mid
        elif capable[mid] == False:
            if (mid + 1) not in capable:
                capable[mid + 1] = is_capable(n, k, w, mid + 1)

            if capable[mid + 1] == True:
                ans = mid + 1
                break
            else:
                bottom = mid + 1

    print(ans)
    # print(capable)