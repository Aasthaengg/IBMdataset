#!/usr/bin/env python
# coding: utf-8

# In[9]:


import collections


# In[32]:


N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))


# In[34]:


t_count = collections.Counter(T)
d_count = collections.Counter(D)

for key,c in t_count.items():
    if key in d_count.keys():
        if d_count[key] < c:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")


# In[ ]:




