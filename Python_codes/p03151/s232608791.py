import bisect
from itertools import accumulate
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(B) > sum(A):
    print(-1)
else:
    donor = []
    acceptance = []
    for a, b in zip(A, B):
        if a > b:
            donor.append(a-b)
        elif a < b:
            acceptance.append(b-a)
    donor.sort(reverse=True)

    ans = len(acceptance)
    ans += bisect.bisect_left([0]+list(accumulate(donor)), sum(acceptance))
    print(ans)
