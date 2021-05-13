import sys
sys.setrecursionlimit(10**6)

import math

a2e = [int(input()) for _ in range(5)]

def get_ceiled_num(num):
    ret = math.ceil(num/10)*10
    return ret

#diff_a2e = [i-get_ceiled_num(i) for i in a2e]
#
#idxs = [i[0] for i in sorted(enumerate(diff_a2e), key=lambda x:-x[1])]
#
#ans = 0
#
#for idx in idxs[:-1]:
#    ans += get_ceiled_num(a2e[idx])
#
#ans += a2e[idxs[-1]]
#    
#print(ans)

ceiled_a2e = [get_ceiled_num(i) for i in a2e]

tot = sum(ceiled_a2e)

ans = tot

for i,j in zip(a2e, ceiled_a2e):
    tmp = tot-(j-i)
    ans = min(ans, tmp)
    
print(ans)