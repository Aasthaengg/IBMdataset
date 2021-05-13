#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math


# In[1]:


N,K = map(int, input().split())


# In[10]:


if K%2 == 0:
    ans = (N//K)**3 + (N//(K//2) - N//K)**3
else:
    ans = (N//K)**3
print(ans)


# In[ ]:




