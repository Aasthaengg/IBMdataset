#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
from functools import reduce


# In[9]:


N = int(input())
T = []
for _ in range(N):
    T.append(int(input()))


# In[10]:


def lcm_base(x,y):
    return (x*y)//math.gcd(x,y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


# In[11]:


print(lcm_list(T))


# In[ ]:




