import math
n,k = map(int,input().split())
li = list(map(int,input().split()))
li.reverse()
count = 0
#print(li)
for i,l in enumerate(li):
    if i != len(li)-1: 
        a = len(list(filter(lambda x:x > l, li[i+1:])))
        count += a

next_count = 0
#print(li)
for i,l in enumerate(li):
    a = len(list(filter(lambda x:x > l, li)))
    next_count += a
""" 
al = 0
for x in range(1,k+1):
    if x == 1:
        al += count
    else:
        al += count
        al += next_count*(x-1) """
#print(al)
all_count = (k+1)*(k)//2
#print(all_count-k,count,next_count)
al = (all_count-k)*(next_count)+k*count
print(al%(10**9+7))
#print(count,next_count)