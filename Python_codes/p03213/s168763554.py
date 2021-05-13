from math import factorial
from itertools import permutations

N = int(input())
n_p = factorial(N)

p_list=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

ans = []
for p1,p2,p3 in permutations(p_list,3):
    n1 = (p1 ** 4) * (p2 ** 4) * (p3 ** 2)
    n2 = (p1 ** 14) * (p2 ** 4)
    n3 = (p1 ** 24) * (p2 ** 2)
    n4 = p1 ** 74
    
    for v in [n1,n2,n3,n4]:
        if n_p % v == 0:
            ans.append(v)
            
print(len(set(ans)))