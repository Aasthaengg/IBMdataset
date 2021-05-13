N, H = map(int, input().split())
alist = []
blist = []
for i in range(N):
    A, B = map(int, input().split())
    alist.append(A)
    blist.append(B)

maxa = max(alist)
blist = list(filter(lambda el: el > maxa, blist))

def mergesort(l):
    def merge(left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        return result + left + right

    length = len(l)
    if length <= 1:
        return l
    middle = length // 2
    return merge(mergesort(l[:middle]), mergesort(l[middle:]))

blist = mergesort(blist)
blist.reverse()

sum_for_h = 0
ans = 0
for i in blist:
    sum_for_h += i
    ans += 1
    if sum_for_h >= H:
        print(ans , flush=True)
        exit()

anum = (H-sum_for_h) / maxa
import math
anum = math.ceil(anum)
print(ans + anum, flush=True)

