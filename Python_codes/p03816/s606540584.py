import math
import collections
N = int(input())
A = list(map(int,input().split()))
A_collections = collections.Counter(A)
ans=N
cut=0
for comp in A_collections.values():
	cut+= comp-1
cut = math.ceil(cut/2)*2
print(ans-cut)