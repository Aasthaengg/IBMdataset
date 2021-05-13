import heapq
pqr = list(map(int,input().split()))
print(sum(heapq.nsmallest(2,pqr)))
