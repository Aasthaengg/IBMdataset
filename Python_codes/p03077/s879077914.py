import math
N = int(input())
lst = [int(input()) for _ in range(5)]

#print(lst)
#print(min(lst),N//min(lst))
'''
if min(lst) >= N:
    print(5)
else:
    print(N//min(lst)+5)
'''

print(math.ceil(N/min(lst))+4)