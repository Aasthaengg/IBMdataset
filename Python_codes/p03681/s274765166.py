#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math


# In[17]:


N,M = map(int, input().split())


# In[18]:


if abs(N-M) > 1:
    ans = 0
else:
    ans = math.factorial(N)*math.factorial(M)
    if N == M:
        ans *= 2
print(ans%(10**9+7))


# In[ ]:




