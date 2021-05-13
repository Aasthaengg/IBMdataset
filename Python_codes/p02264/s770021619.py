# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 14:42:43 2018

@author: maezawa
"""

def print_array(g):
    ans = str(g[0])
    if len(g) > 1:
        for i in range(1,len(g)):
            ans += ' '+str(g[i]) 
    print(ans)

name=[]
time=[]
current_time = 0

n, q = list(map(int, input().split()))
for i in range(n):
    s = input().split()
    name.append(s[0])
    time.append(int(s[1]))
# =============================================================================
# print(n,q)
# print(name)
# print(time)
# =============================================================================
finished = []
fin_time = []
i=0
remain = n
while True:
    if time[i] <= q:
        current_time += time.pop(i)
        finished.append(name.pop(i))
        fin_time.append(current_time)      
        remain -= 1
        if remain == 0:
            break
        i = i%remain
    else:
        time[i] -= q
        current_time += q
        i = (i+1)%remain

for i in range(n):
    print("{} {}".format(finished[i], fin_time[i]))
        
    
