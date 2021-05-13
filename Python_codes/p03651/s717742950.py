#!/usr/bin/env python
# coding: utf-8

# In[11]:


import math
from functools import reduce


# In[17]:


N,K = map(int, input().split())
A = list(map(int, input().split()))


# In[18]:


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


# In[19]:


g = gcd_list(A)
if K <= max(A) and K%g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")


# In[ ]:




