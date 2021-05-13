#!/usr/bin/env python
# coding: utf-8

# In[5]:


h,w,m = map(int, input().split())
hw_list = []
for _ in range(m):
    hw_list.append(list(map(int, input().split())))


# In[6]:


def solve(h,w,m,hw_list):
    h_count = [0]*(h+1)
    w_count = [0]*(w+1)
    for h_,w_ in hw_list:
        h_count[h_] += 1
        w_count[w_] += 1
        
    h_max = max(h_count)
    w_max = max(w_count)
    ans = h_max + w_max
    
    h_max_count = 0
    w_max_count = 0
    for i in range(h+1):
        if h_count[i] == h_max:
            h_max_count += 1
    for j in range(w+1):
        if w_count[j] == w_max:
            w_max_count += 1
    
    max_count = h_max_count*w_max_count
    max_count_cross = 0
    for h_,w_ in hw_list:
        if h_count[h_] == h_max and w_count[w_] == w_max:
            max_count_cross += 1
    
    if max_count_cross == max_count:
        ans -= 1
    
    return ans


# In[7]:


ans = solve(h,w,m,hw_list)
print(ans)


# In[ ]:




