import copy
from collections import Counter

N = int(input())
K = list(map(int,input().split()))
"""
N = 4
K = [1, 2 ,3 ,4]
"""
a = list(set(K))
#print(a)
a_count = {}



a_count = Counter(K)
#print(c)

#print(a_count)

ans_dict = 0
for l in a_count.values() :
        
    ans_dict += l * (l-1)  // 2

#print(ans_dict)

"""
for i in a_count :

    a_count_2 = copy.deepcopy(a_count)
    
    a_count_2[i] -= 1

    #print(a_count_2)
    
    ans_dict[i] = 0
    for l in a_count_2.values() :
        
        ans_dict[i] += l * (l-1)  // 2

#print(ans_dict)
"""

for i in K:
    print(ans_dict - (a_count[i]-1))
    pass