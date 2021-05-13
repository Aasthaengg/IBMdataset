# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:13:00 2020

@author: msaleh1
"""

def upper_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = int(l + (r - l) / 2)
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l


mx = pow(10,100)
#pypy3
s = input()
t = input()

    
cnt_s = dict()
cnt_t = dict()

for c in t:
    if c in cnt_t:
        cnt_t[c]+=1
    else:
        cnt_t[c] = 1


for idx in range(len(s)):
    if s[idx] in cnt_s:
        cnt_s[s[idx]].append(idx)  
    else:
       cnt_s[s[idx]] = [idx]

#cannot
for x in cnt_t:
    if x not in cnt_s:
        print(-1)
        exit(0)
    else:
        if(cnt_t[x] > mx*len(cnt_s[x])):
            print(-1)
            exit(0)
            
cur_indx =-1
skp =0
ans = 0

for x in t:
    temp_idx = upper_bound(cnt_s[x],cur_indx)
    if(temp_idx == len(cnt_s[x])):
        skp+=1
        cur_indx = cnt_s[x][0]
    else:
        cur_indx = cnt_s[x][temp_idx];
if(skp >= mx):
    print(-1)
else:
    print(skp*len(s)+cur_indx+1)
