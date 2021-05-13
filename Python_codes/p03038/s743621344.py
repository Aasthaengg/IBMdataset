N, M = map(int, input().split())
A = list(map(int, input().split()))

import numpy as np
import collections

count = 0
BC = []

# Python code to sort the tuples using second element  
# of sublist Inplace way to sort using sort() 
def Sort(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li 

for i in range (0, M):
	BC.append(list(map(int, input().split())))
    
BC = collections.deque(reversed(Sort(BC)))

Secondlist = []

V = 0

while count < N and BC:
	V = BC.popleft()
	for i in range (0, V[0]):
		Secondlist.append(V[1])
		count+=1

C = A+Secondlist
C = sorted(C, reverse = True)
print(sum(C[:N]))