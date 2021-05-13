#!/usr/bin/env python
# coding: utf-8

# In[9]:


N = int(input())
a = list(map(int, input().split()))


# In[12]:


a_s = sorted(a, reverse=True)
print(sum(a_s[1:N*2:2]))


# In[ ]:




