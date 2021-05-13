import sys
import heapq


input = sys.stdin.readline
n, m = map(int, input().split())
a_list = list(map(int, input().split()))
a_list = list(map(lambda x: x*(-1), a_list))
heapq.heapify(a_list)

while m > 0:
    max_a = heapq.heappop(a_list)
    heapq.heappush(a_list, (-1)*(-max_a//2))
    m -= 1

print(-sum(a_list))
