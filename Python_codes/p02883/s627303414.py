import math
n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]

a.sort()
f.sort(reverse=True)

af = [[a[i]*f[i], a[i], f[i]] for i in range(n)]
af.sort(reverse=True)

def check(mid):
    count = 0
    for i in range(n):
        num = math.ceil((af[i][0] - mid) / af[i][2])
        if num > af[i][1]:
            return False
        else:
            count += num
            if count > k:
                return False
    else:
        return True

# https://qiita.com/hamko/items/794a92c456164dcc04ad
def binary_search():
    ng = -1 # left:絶対に達成不可能なもの
    ok = 10**13 # right:絶対に達成可能なもの
    while (ok - ng > 1):
        mid = (ng + ok) // 2
        if check(mid) == True:
            ok = mid
        else:
            ng = mid
    return ok
print(binary_search())
