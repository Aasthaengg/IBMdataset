import sys
import heapq

array_pqr = list(map(int,input().split()))

if not ( 1 <= array_pqr[0] <= 100 and 1 <= array_pqr[1] <= 100 and 1 <= array_pqr[2] <= 100 ): sys.exit()

print(sum(heapq.nsmallest(2,array_pqr)))