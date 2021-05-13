from bisect import bisect_right
import itertools

N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
acum = list(itertools.accumulate(a))

answer = bisect_right(acum, x)
if answer == N:
    if acum[-1] < x:
        answer -= 1
print(answer)
