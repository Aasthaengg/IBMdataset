import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
a = LI()
count = 0
a_dict = {}
for i,x in enumerate(a,1):
    a_dict[i] = x
for k,v in a_dict.items():
    if k in [a_dict[v]]:
        count +=1
print(count//2)
