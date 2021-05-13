import heapq
N, K = map(int, input().split())
L = list(map(int, input().split()))
print(sum(heapq.nlargest(K,L)))