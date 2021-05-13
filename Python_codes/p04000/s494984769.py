import collections
import sys
input = sys.stdin.readline

h, w, n = [ int(v) for v in input().split() ]
ans_list = [ 0 for i in range(10) ]
ans_list[0] = (h-2)*(w-2) 
adjust_counter = collections.Counter([])
adjust_list = [ [i,j] for i in range(-1,2) for j in range(-1,2)]


def makehash(a,b):
    return a*10**9+b

for i in range(n):
    a, b = [ int(v) - 1 for v in input().split() ]
    for j in adjust_list:
        p, q = j
        if 1 <= p+a <= h-2 and 1 <= q+b <= w-2:
            c = adjust_counter[makehash(p+a,q+b)]
            adjust_counter[makehash(p+a,q+b)] += 1
            ans_list[c] -= 1
            ans_list[c+1] += 1

for i in ans_list:
    print(i)