#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
from functools import reduce


# In[19]:


N = int(input())
a = list(map(int, input().split()))


# In[20]:


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


# In[21]:


f = 0
m = lcm_list(a)-1
for i in range(N):
    f += m%a[i]
print(f)


# In[ ]:




