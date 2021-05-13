#!/usr/bin/env python
# coding: utf-8

# In[2]:


import collections


# In[11]:


N = int(input())
S = input()


# In[13]:


ans = 1
for tmp in collections.Counter(S).items():
    x = tmp[1]+1
    ans *= x
print((ans-1)%(10**9+7))


# In[ ]:




