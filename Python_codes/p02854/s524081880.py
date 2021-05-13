from itertools import accumulate
import bisect

n = int(input())
a = list(map(int, input().split()))

acc = list(accumulate(a))

#idx = bisect.bisect_left(acc,acc[-1]//2)
#print(idx)
result = []
for i in range(n):
    result.append(abs((acc[-1] - acc[i] ) - acc[i]))
print(min(result))