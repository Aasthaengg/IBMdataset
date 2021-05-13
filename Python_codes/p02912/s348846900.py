from heapq import heappush, heappop, heapify

def neg_int(n):
    return -int(n)
    
N, M = map(int, input().split())
a_list = list(map(neg_int, input().split()))
heapify(a_list)
for _ in range(M):
    a = -heappop(a_list)
    a //= 2
    heappush(a_list, -a)
print(-sum(a_list))