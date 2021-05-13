from  heapq import heappush, heappop, heapify
import math

N, K = map(int, input().split())

A = list(map(int, input().split()))

l = 0
r = 10 ** 9

def check(m):
    now = 0
    for i in range(N):
        #A[i]-1してるのは、たとえばm=3のときは4,7から回数が増えるため
        now += (A[i]-1) // m
    return now <= K

#差が1になったら終了
while r - l > 1:
    m = (l + r) // 2

    if check(m):
        r = m
    else:
        l = m

print(r)